# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-01 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0011_remove_article_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_headline', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
