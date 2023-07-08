import asyncio
import json
from typing import Any, Optional, Callable, Dict

from django.http import HttpResponse
from asgiref.sync import sync_to_async
from rest_framework.serializers import Serializer

from base.entity.entity import Entity
from base.integration.base_use_case import BaseUseCase
from base.integration.base_sync_view import BaseSyncView

class BaseAsyncView(BaseSyncView):
    sync_fun: Optional[Callable[[Any], HttpResponse]] = None

    async def post(self, request, *args, **kwargs):
        return await self._process(request, *args, **kwargs)

    async def get(self, request, *args, **kwargs):
        return await self._process(request, *args, **kwargs)

    async def _process(self, request, *args, **kwargs) -> HttpResponse:
        data: Dict[str, Any] = self._prepare_parameters(request, *args, **kwargs)
        kwargs["data"] = data
        serializer: Serializer = self.get_serializer(*args, **kwargs)
        serializer.is_valid(raise_exception=True)
        club_id: Optional[int] = self._get_club_id(data)
        use_case: BaseUseCase = self._get_use_case(club_id)
        try:
            result: Entity = await self.execute(use_case, serializer)
        except NotImplementedError as error:
            # support old sync view functions. Delete later whe all methods will be rewritten and documented
            if self.sync_fun:
                return await sync_to_async(self.sync_fun)(request, *args, **kwargs)
            else:
                raise error
        response = self.get_response(result)
        response["Handler-type"] = "async"
        return response

    async def execute(self, use_case: BaseUseCase, serializer: Serializer) -> Entity:
        return await use_case.execute(**serializer.validated_data)

    # https://github.com/encode/django-rest-framework/issues/7260
    # todo modified DRF dispatch method to enable async support
    # todo temp solution, waiting for DRF async feature support
    async def dispatch(self, request, *args, **kwargs):
        """Add async support.
        """
        self.args = args
        self.kwargs = kwargs
        user = None
        if hasattr(request, "user"):
            user = request.user
        request = self.initialize_request(request, *args, **kwargs)
        request.user = user
        self.request = request
        self.headers = self.default_response_headers

        try:
            await sync_to_async(self.initial)(
                request, *args, **kwargs)  # MODIFIED HERE

            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(),
                                  self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed

            # accept both async and sync handlers
            # built-in handlers are sync handlers
            if not asyncio.iscoroutinefunction(handler):  # MODIFIED HERE
                handler = sync_to_async(handler)  # MODIFIED HERE
            response = await handler(request, *args, **kwargs)  # MODIFIED HERE

        except Exception as exc:
            response = self.handle_exception(exc)

        self.response = self.finalize_response(
            request, response, *args, **kwargs)
        return self.response

    @classmethod
    def as_view(cls, *args, **initkwargs):
        """Make Django process the view as an async view.
        """
        view = super().as_view(*args, **initkwargs)

        async def async_view(*args, **kwargs):
            # wait for the `dispatch` method
            return await view(*args, **kwargs)

        return async_view
