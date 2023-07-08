from django.contrib import admin
from attachments.models import Attachment, OnlineMaterialCategory

class AttachmentAdmin(admin.ModelAdmin):
    search_fields = ['title__icontains', 'club__name']
    list_filter = ['club']

admin.site.register(Attachment, AttachmentAdmin)
admin.site.register(OnlineMaterialCategory)
