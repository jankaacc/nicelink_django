# Generated by Django 2.1.dev20171019014353 on 2017-10-26 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nicelink', '0006_remove_usermodel_links'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='link_user',
            field=models.ForeignKey(default=1 , on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
