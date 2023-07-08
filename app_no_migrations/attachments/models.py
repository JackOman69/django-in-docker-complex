from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _
from django.core import serializers 
from fitness.settings import BASE_URL
from organization.models import Club
import os
import json

def attachment_upload(instance, filename):
    return 'attachments/{name}_{category}/{filename}'.format(
        name=instance.title,
        category=instance.category.name,
        filename=filename
    )

class AttachmentManager(models.Manager):
    def attachments_for_object(self, obj):
        object_type = ContentType.objects.get_for_model(obj)
        return self.filter(content_type__pk=object_type.id,
                           object_id=obj.pk)
        
    def as_json(self, club_object):
        queryset = Attachment.objects.filter(club=club_object)
        attachment = json.loads(serializers.serialize(
            'json', 
            queryset=queryset, 
            fields=('title', 'link', 'attachment_file', 'category',)
        ))
        
        for i in attachment:
            for j in queryset:
                i['fields']['attachment_file'] = f'https://{BASE_URL}/media/{i["fields"]["attachment_file"]}'
                i['fields']['category'] = j._meta.get_field('category')
            
        result = [a['fields'] for a in attachment]
        return result

class OnlineMaterialCategory(models.Model):
    club = models.ForeignKey(
        Club, models.SET_NULL,
        verbose_name="Клуб",
        blank=True,
        null=True
    )
    name = models.CharField(max_length=2550, default='', verbose_name='название')
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['-name']
    
    def __str__(self):
        return self.name


class Attachment(models.Model):
    objects = AttachmentManager()
    
    club = models.ManyToManyField(Club, verbose_name="клубы", blank=True)
    title = models.CharField(max_length=255, default='', verbose_name='Название')
    link = models.CharField(max_length=255, default='', blank=True, verbose_name='ссылка')
    attachment_file = models.FileField(_('файл'), null=True, blank=True, upload_to=attachment_upload)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)
    category = models.ForeignKey(
        OnlineMaterialCategory, models.SET_NULL,
        verbose_name="Категория",
        blank=True,
        null=True
    )
    
    class Meta:
        verbose_name = "Полезный материал"
        verbose_name_plural = "Полезные материалы"
        ordering = ['-modified']
    
    def __str__(self):
        return self.title
    
    def as_json(self):
        try:
            file = BASE_URL + self.attachment_file.url
        except ValueError:
            file = ""
        
        return dict(
            title=self.title,
            link=self.link,
            file=file,
            category=self.category.name
        )
        
    @property
    def filename(self):
        return os.path.split(self.attachment_file.name)[1]