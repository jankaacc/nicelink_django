# Generated by Django 2.1.dev20171019014353 on 2017-10-21 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nicelink', '0003_auto_20171020_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='oryginal_link_text',
            field=models.URLField(),
        ),
    ]