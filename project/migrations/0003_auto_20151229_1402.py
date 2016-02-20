# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20151229_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='long_description',
            field=models.TextField(),
        ),
    ]
