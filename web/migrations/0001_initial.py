# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-12 06:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('company', models.CharField(max_length=128)),
                ('telephone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name',),
                'db_table': 'contact',
                'verbose_name': 'contact',
                'verbose_name_plural': 'contacts',
            },
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ('email',),
                'db_table': 'subscribe',
                'verbose_name': 'subscribe',
                'verbose_name_plural': 'subscribes',
            },
        ),
    ]
