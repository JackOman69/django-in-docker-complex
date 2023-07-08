from dataclasses import dataclass

from base.entity.entity import Entity


@dataclass
class Banner(Entity):
    name: str
    description: str
    file: str
