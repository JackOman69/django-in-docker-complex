from django.urls import re_path
from banners.api.get_banners.views import GetBannersView

urlpatterns = [
    re_path(r'^get_banners/$', GetBannersView.as_view(), name='get_banners')
]