from abc import ABC, abstractmethod
from base.entity.entity import Entity
from base.integration.abstract_backend import Backend
from base.entity.user_profile import UserProfile
from typing import List, Any, Optional

class BaseSyncUseCase(ABC):
    def __init__(self, backend: Backend, user_profile: Optional[UserProfile]):
        self.backend: Backend = backend
        self.user_profile: Optional[UserProfile] = user_profile

    @abstractmethod
    def execute(self, **kwargs) -> Entity:
        ...

    def prepare_list_data(self, data) -> List[Any]:
        return self.prepare_data(data) or []

    def prepare_data(self, data):
        if isinstance(data, NotImplementedError):
            raise NotImplementedError

        if isinstance(data, BaseException):
            try:
                raise data
            except Exception:
                pass
            return None
        else:
            return data

class BaseUseCase(BaseSyncUseCase):
    @abstractmethod
    async def execute(self, **kwargs) -> Entity:
        ...
