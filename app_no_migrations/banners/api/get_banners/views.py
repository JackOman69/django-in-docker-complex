from base.integration.base_async_view import BaseAsyncView
from banners.api.get_banners.use_case import GetBannersUseCase
from banners.api.get_banners.serializer import GetBannersSerializer

class GetBannersView(BaseAsyncView):
    serializer_class = GetBannersSerializer
    use_case_class = GetBannersUseCase