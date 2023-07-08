import os
from django.contrib.auth.models import User
from django.db import models
from integration.models import Server
from fitness.settings import BASE_URL


def get_image_path(instance, filename):
    return os.path.join('profile', filename)


class Club(models.Model):
    server = models.ForeignKey(Server, null=True, blank=True, on_delete=models.CASCADE, verbose_name='сервер')
    name = models.CharField(max_length=255, verbose_name='название', default='')
    club_id = models.IntegerField(verbose_name='club_id клуба', default=None, null=True, blank=True)
    phone = models.CharField(max_length=30, verbose_name='телефон', default='', blank=True)
    address = models.CharField(max_length=255, verbose_name='адрес', default='', blank=True)
    vk_news_domain = models.CharField(max_length=100, verbose_name='группа ВК', default='', blank=True)
    fb_news_domain = models.CharField(max_length=100, verbose_name='группа Facebook', default='', blank=True)
    instagram = models.CharField(max_length=1000, verbose_name='инстаграм', default='', blank=True)
    twitter = models.CharField(max_length=1000, verbose_name='твитер', default='', blank=True)
    website = models.CharField(max_length=1000, verbose_name='сайт', default='', blank=True)
    work_hours = models.TextField(verbose_name='время работы', default='', blank=True)
    latitude = models.FloatField(verbose_name='широта', default=0, blank=True)
    longitude = models.FloatField(verbose_name='долгота', default=0, blank=True)
    email = models.EmailField(default='', blank=True)
    user = models.OneToOneField(User, verbose_name='администратор', null=True, blank=True,
                                limit_choices_to={'groups__name': 'Администрация клуба'},
                                on_delete=models.deletion.SET_NULL)
    logo = models.ImageField(upload_to=get_image_path, verbose_name='Лого', default='', blank=True)

    def club_data(self):
        return dict(
            id=self.id,
            name=self.name
        )

    def as_json(self):
        return dict(
            id=self.id,
            name=self.name,
            phone=self.phone,
            address=self.address,
            vk_news_domain=self.vk_news_domain,
            fb_news_domain=self.fb_news_domain,
            instagram=self.instagram,
            twitter=self.twitter,
            website=self.website,
            work_hours=self.work_hours,
            latitude=self.latitude,
            longitude=self.longitude,
            email=self.email
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'клуб'
        verbose_name_plural = 'клубы'


class BaseClubModel(models.Model):
    club = models.ForeignKey(Club, default=1, on_delete=models.deletion.SET_DEFAULT)

    class Meta:
        abstract = True
