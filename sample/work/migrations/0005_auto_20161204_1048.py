# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-04 10:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0004_stan_reponse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stan',
            name='ques',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='work.Question'),
        ),
    ]
