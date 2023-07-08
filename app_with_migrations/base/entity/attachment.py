from dataclasses import dataclass

from base.entity.entity import Entity


@dataclass
class Attachment(Entity):
    title: str
    file: str
    category: str
    link: str = ""
