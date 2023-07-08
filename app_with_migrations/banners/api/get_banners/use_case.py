from base.integration.base_use_case import BaseUseCase
from organization.models import Club
from banners.models import BannersModel
from integration.models import Server
from banners.api.get_banners.result import GetBannersResult
from base.integration.exceptions import ErrorWithMessage
import os
from typing import Mapping, Any, Optional

class GetBannersUseCase(BaseUseCase):
    
    async def execute(self, server_name: Optional[str] = None, club_id: Optional[int] = None) -> GetBannersResult:
        os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
        if server_name and club_id:
            server_name: str = server_name.title()
            try:
                server_object = Server.objects.get(title=server_name)
                club_object = Club.objects.filter(server=server_object).get(club_id=club_id)
                banners = BannersModel.objects.filter(club=club_object)
            except:
                raise ErrorWithMessage("Не найдено совпадений", "Такого сервера или клуба не существует")
        else:    
            banners = BannersModel.objects.all()
        
        result: Mapping[str, Any] = sorted([banner_object.as_json() for banner_object in banners], key=lambda x:x["sort"])
        sorted_result: Mapping[str, Any] = [{k:v for k,v in i.items() if k != "sort"} for i in result]
        
        return GetBannersResult(banners=sorted_result)
        