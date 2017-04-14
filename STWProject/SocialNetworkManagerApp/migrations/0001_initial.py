# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-14 11:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Complement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(max_length=300)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='complement',
            name='id_network',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SocialNetworkManagerApp.Network'),
        ),
        migrations.AddField(
            model_name='box',
            name='complement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SocialNetworkManagerApp.Complement'),
        ),
        migrations.AddField(
            model_name='box',
            name='id_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='box',
            name='network',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SocialNetworkManagerApp.Network'),
        ),
    ]