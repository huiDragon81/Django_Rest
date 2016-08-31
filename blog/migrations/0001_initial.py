# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('reg_date', models.DateTimeField(auto_created=True, auto_now=True)),
                ('title', models.CharField(max_length=256)),
                ('contents', models.CharField(max_length=2048)),
            ],
        ),
    ]
