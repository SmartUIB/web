# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 11:14
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('public', models.BooleanField()),
                ('email', models.EmailField(max_length=254, null=True)),
                ('challenge', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='idea_challenge', to='homepage.Challenge')),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('url', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('media', models.ImageField(upload_to='media')),
            ],
        ),
    ]