# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 22:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_shelf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('body', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='num_reviews',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bookreview',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_shelf.Book'),
        ),
        migrations.AddField(
            model_name='bookreview',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='book_shelf.User'),
        ),
    ]
