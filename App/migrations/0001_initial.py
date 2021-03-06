# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 06:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btitle', models.CharField(max_length=20)),
                ('bname', models.CharField(max_length=20)),
                ('bcount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=20)),
                ('cinfo', models.CharField(max_length=200)),
                ('ctitle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Blog')),
            ],
        ),
    ]
