import datetime

from dataclasses import dataclass
from typing import Optional

from base.entity.entity import Entity


@dataclass
class UserProfile(Entity):
    crm_id: str
    club_id: int = 0
    user_id: int = 0
    auth_token: str = ""
    token: str = ""
    salt: str = ""
    auth_scheme: str = ""
    profile_id: int = 0
    username: str = ""
    name: str = ""
    last_name: str = ""
    second_name: str = ""
    email: str = ""
    image_url: str = ""

    # backwards
    image: str = ""

    phone: str = ""
    is_chat_blocked: bool = False
    is_staff: bool = False
    is_admin: bool = False
    role: str = ""
    birth_date: Optional[datetime.date] = None
    # additional parameters
    is_payed: Optional[bool] = None
    status: str = ""
    cost: float = 0
    block_workout_date: Optional[datetime.date] = None
    sex: Optional[str] = None
    disabled: Optional[bool] = None

    def full_name(self):
        return f"{self.name} {self.second_name} {self.last_name}".strip().replace("  ", ' ')

    def full_name_last_name_first(self):
        return f"{self.last_name} {self.name} {self.last_name}".strip().replace("  ", " ")

    def is_filled_base_info(self) -> bool:
        return not (not self.crm_id or not self.name or not self.last_name or not self.image_url)

    @staticmethod
    def empty() -> "UserProfile":
        return UserProfile(
            crm_id="",
            name="",
            last_name="",
            second_name="",
            image_url="",
            phone=""
        )
