from django.urls import re_path
from attachments.api.get_attachment.views import GetAttachmentView

urlpatterns = [
    re_path(r'^get_attachment/$', GetAttachmentView.as_view(), name='get_attachment')
]