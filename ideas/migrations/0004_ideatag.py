# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0003_auto_20170520_0321'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdeaTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_text', models.CharField(max_length=10)),
            ],
        ),
    ]
