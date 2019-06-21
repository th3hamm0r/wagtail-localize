# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-28 15:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_localize', '0009_region_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ['-is_active', 'code']},
        ),
        migrations.AlterModelOptions(
            name='locale',
            options={'ordering': ['-is_active', '-region__is_default', 'region__name', 'language__code']},
        ),
    ]