# Generated by Django 4.1.7 on 2023-03-07 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
        ('attachments', '0004_remove_attachment_club_attachment_club'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='club',
            field=models.ManyToManyField(blank=True, to='organization.club', verbose_name='клубы'),
        ),
    ]
