# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20151229_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='long_description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
