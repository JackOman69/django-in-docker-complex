from django.db import models
from fitness.settings import BASE_URL
from organization.models import Club

def banner_upload(instance, filename):
    return 'banners/{name}/{filename}'.format(
        name=instance.name,
        description=instance.description,
        filename=filename
    )

class BannersModel(models.Model):
    club = models.ForeignKey(
        Club, models.SET_NULL,
        verbose_name="Привязка к клубу",
        blank=True,
        null=True
    )
    name = models.CharField(max_length=150, verbose_name="Название баннера", default="", blank=True, null=True)
    description = models.TextField(verbose_name="Многострочное описание баннера", default="", blank=True, null=True)
    image = models.ImageField(upload_to=banner_upload, verbose_name="Изображение баннера", blank=True, null=True)
    sort = models.IntegerField(default=500, verbose_name="Сортировка")
    
    class Meta:
        verbose_name_plural = "Баннеры"
        
    def as_json(self):
        try:
            file = BASE_URL + self.image.url
        except ValueError:
            file = ""
        
        return dict(
            name=self.name,
            description=self.description,
            image=file,
            sort=self.sort
        )