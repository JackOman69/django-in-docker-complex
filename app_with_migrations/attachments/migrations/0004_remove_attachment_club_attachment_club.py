# Generated by Django 4.1.7 on 2023-02-23 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
        ('attachments', '0003_alter_attachment_attachment_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachment',
            name='club',
        ),
        migrations.AddField(
            model_name='attachment',
            name='club',
            field=models.ManyToManyField(blank=True, null=True, to='organization.club', verbose_name='клубы'),
        ),
    ]