from django.contrib import admin
from .models import BannersModel

class BannersAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "image")

admin.site.register(BannersModel, BannersAdmin)