from dataclasses import dataclass
from typing import List

from base.entity.entity import Entity
from base.entity.banner import Banner as BannerEntity


@dataclass
class GetBannersResult(Entity):
    banners: List[BannerEntity]