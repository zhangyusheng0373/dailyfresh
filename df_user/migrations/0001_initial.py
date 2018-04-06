# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('upassword', models.CharField(max_length=40)),
                ('uemall', models.CharField(max_length=30)),
                ('ushou', models.CharField(max_length=20)),
                ('uaddress', models.CharField(max_length=100)),
                ('uyoubian', models.CharField(max_length=6)),
                ('uphoto', models.CharField(max_length=11)),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
    ]
