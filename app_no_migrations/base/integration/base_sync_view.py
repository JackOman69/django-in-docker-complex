import json
import dataclasses
from typing import Optional, Mapping, Any, Dict

from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework.serializers import Serializer

from base.entity.entity import Entity
from base.entity.user_profile import UserProfile
from base.utils.base_utils import date_converter
from base.integration.base_use_case import BaseSyncUseCase, BaseUseCase
from base.integration.exceptions import BadParameterException, UseCaseIsNotSetException

class BaseSyncView(GenericAPIView):
    IGNORED_GET_PARAMETERS = ["token"]

    serializer_class = Serializer
    response_serializer_class = None
    use_case_class = None
    default_url_argument = "club_id"
    find_profile_by_header_club_id = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_profile: Optional[UserProfile] = None

    def post(self, request, *args, **kwargs):
        return self._process(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self._process(request, *args, **kwargs)

    def _get_use_case(self, club_id: Optional[int]) -> BaseUseCase:
        if self.use_case_class is None:
            raise UseCaseIsNotSetException()
        backend = None
        return self.use_case_class(backend, self.user_profile)

    def _serialize_result(self, result: Entity) -> Mapping[str, Any]:
        dictionary = dataclasses.asdict(result)
        if self.response_serializer_class is None:
            return dictionary
        return self.response_serializer_class(dictionary).data

    def _prepare_multipart_parameters(self, request) -> Mapping[str, Any]:
        parameters: Dict[str, Any] = {}
        for key in request.data:
            value = request.data[key]
            if isinstance(value, list):
                if len(value) > 1:
                    raise BadParameterException()
                elif len(value) == 0:
                    continue
                else:
                    parameters[key] = value[0]
            else:
                parameters[key] = value
        return parameters

    def __prepare_get_parameters(self, request) -> Mapping[str, Any]:
        parameters: Dict[str, Any] = {}
        for key in request.GET:
            if key in self.IGNORED_GET_PARAMETERS:
                continue
            value = request.GET[key]
            if isinstance(value, list) or isinstance(value, tuple):
                if len(value) > 1:
                    raise BadParameterException()
                elif len(value) == 0:
                    continue
                else:
                    parameters[key] = value[0]
            else:
                parameters[key] = value
        return parameters

    def _prepare_url_parameters(self, *args) -> Mapping[str, Any]:
        if isinstance(args, tuple) and len(args) == 1:
            try:
                return {
                    self.default_url_argument: int(args[0])
                }
            except Exception:
                return {}
        else:
            return {}

    def get_response(self, result: Entity):
        return HttpResponse(json.dumps(self._serialize_result(result), default=date_converter),
                            content_type='application/json; charset=utf-8')

    def execute(self, use_case: BaseSyncUseCase, serializer: Serializer) -> Entity:
        return use_case.execute(**serializer.validated_data)

    def _prepare_parameters(self, request, *args, **kwargs) -> Dict[str, Any]:
        data: Dict[str, Any] = {}
        data.update(self.__prepare_get_parameters(request))
        data.update(self._prepare_url_parameters(*args))
        data.update(request.data)
        return data

    def _get_club_id(self, data: Mapping[str, Any]) -> Optional[int]:
        club_id = data.get("club_id")
        if type(club_id) is str:
            try:
                club_id = int(club_id)
            except Exception as e:
                return None
        if club_id is None and self.user_profile:
            club_id = self.user_profile.club_id

        return club_id

    def _process(self, request, *args, **kwargs) -> HttpResponse:
        self._check_auth(request, *args, **kwargs)
        data: Dict[str, Any] = self._prepare_parameters(request, *args, **kwargs)
        kwargs["data"] = data
        serializer: Serializer = self.get_serializer(*args, **kwargs)
        serializer.is_valid(raise_exception=True)
        club_id: Optional[int] = self._get_club_id(data)
        use_case: BaseSyncUseCase = self._get_use_case(club_id)
        result: Entity = self.execute(use_case, serializer)
        response = self.get_response(result)
        return response

