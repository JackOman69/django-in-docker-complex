from dataclasses import dataclass, field
from typing import List

from base.entity.entity import Entity
from base.entity.attachment import Attachment as AttachmentEntity


@dataclass
class GetAttachmentResult(Entity):
    attachments: List[AttachmentEntity]