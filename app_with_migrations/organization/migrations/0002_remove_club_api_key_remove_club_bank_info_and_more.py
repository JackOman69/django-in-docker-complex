# Generated by Django 4.1.7 on 2023-03-07 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0003_remove_server_club'),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='api_key',
        ),
        migrations.RemoveField(
            model_name='club',
            name='bank_info',
        ),
        migrations.RemoveField(
            model_name='club',
            name='contacts_line_image',
        ),
        migrations.RemoveField(
            model_name='club',
            name='crm_id',
        ),
        migrations.RemoveField(
            model_name='club',
            name='display_text',
        ),
        migrations.RemoveField(
            model_name='club',
            name='news_token',
        ),
        migrations.RemoveField(
            model_name='club',
            name='oferta_url',
        ),
        migrations.RemoveField(
            model_name='club',
            name='phone_number_formatted',
        ),
        migrations.RemoveField(
            model_name='club',
            name='show_in_mobile_settings',
        ),
        migrations.RemoveField(
            model_name='club',
            name='vk_post_header',
        ),
        migrations.AddField(
            model_name='club',
            name='server',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='integration.server', verbose_name='сервер'),
        ),
    ]