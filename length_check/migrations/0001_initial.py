# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('country', models.CharField(max_length=32, serialize=False, primary_key=b'country')),
                ('gdp', models.IntegerField()),
            ],
        ),
    ]
