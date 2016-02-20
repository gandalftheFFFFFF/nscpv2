# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('short_description', models.CharField(max_length=200)),
                ('url', models.URLField(max_length=300)),
                ('long_description', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', verbose_name='Tags', through='taggit.TaggedItem', help_text='A comma-separated list of tags.')),
            ],
        ),
    ]
