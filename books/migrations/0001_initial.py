# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30, verbose_name=b'\xe5\xa7\x93')),
                ('last_name', models.CharField(max_length=40, verbose_name=b'\xe5\x90\x8d')),
                ('email', models.EmailField(max_length=254, verbose_name=b'\xe9\x82\xae\xe4\xbb\xb6\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xe4\xb9\xa6\xe5\x90\x8d')),
                ('publication_date', models.DateField(null=True, verbose_name=b'\xe5\x87\xba\xe7\x89\x88\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('authors', models.ManyToManyField(to='books.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=60)),
                ('state_province', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=50)),
                ('website', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(to='books.Publisher'),
        ),
    ]
