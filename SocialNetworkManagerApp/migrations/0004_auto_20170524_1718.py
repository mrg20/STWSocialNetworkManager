# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-24 17:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SocialNetworkManagerApp', '0003_auto_20170524_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]