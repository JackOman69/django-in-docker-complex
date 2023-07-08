from base.integration.base_use_case import BaseUseCase
from organization.models import Club
from attachments.models import Attachment
from integration.models import Server
from attachments.api.get_attachment.result import GetAttachmentResult
from base.integration.exceptions import ErrorWithMessage
import os
from typing import Mapping, Any

class GetAttachmentUseCase(BaseUseCase):
    
    async def execute(self, server_name: str, club_id: int) -> GetAttachmentResult:
        os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
        server_name: str = server_name.title()
        try:
            server_object = Server.objects.get(title=server_name)
            club_object = Club.objects.filter(server=server_object).get(club_id=club_id)
            attachments = Attachment.objects.filter(club=club_object)
        except:
            raise ErrorWithMessage('Не найдено совпадений', 'Такого сервера или клуба не существует')
        result: Mapping[str, Any] = [attachment_object.as_json() for attachment_object in attachments]
        return GetAttachmentResult(attachments=result)
        