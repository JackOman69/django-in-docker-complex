from base.integration.base_async_view import BaseAsyncView
from attachments.api.get_attachment.use_case import GetAttachmentUseCase
from attachments.api.get_attachment.serializer import GetAttachmentSerializer

class GetAttachmentView(BaseAsyncView):
    serializer_class = GetAttachmentSerializer
    use_case_class = GetAttachmentUseCase