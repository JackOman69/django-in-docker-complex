# Generated by Django 4.1.7 on 2023-02-22 23:17

import attachments.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attachments', '0002_attachment_club'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='attachment_file',
            field=models.FileField(blank=True, null=True, upload_to=attachments.models.attachment_upload, verbose_name='файл'),
        ),
    ]
