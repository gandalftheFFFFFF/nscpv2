# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20151230_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.URLField(max_length=300, blank=True, null=True),
        ),
    ]
