# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-26 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=100)),
                ('card', models.IntegerField()),
                ('movies', models.ManyToManyField(to='api.Movie')),
            ],
        ),
    ]