# Generated by Django 2.1.dev20171019014353 on 2017-10-23 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nicelink', '0004_auto_20171021_1034'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=60, unique=True)),
                ('fullname', models.CharField(max_length=40)),
                ('links', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nicelink.Link')),
            ],
        ),
    ]