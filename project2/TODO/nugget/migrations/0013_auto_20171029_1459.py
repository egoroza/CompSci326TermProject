# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 18:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nugget', '0012_auto_20171029_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nuggetattribute',
            name='battle_xp',
        ),
        migrations.AddField(
            model_name='nuggetattribute',
            name='battle_XP',
            field=models.ForeignKey(default='0', null=True, on_delete=django.db.models.deletion.SET_NULL, to='nugget.Battle'),
        ),
        migrations.AlterField(
            model_name='battle',
            name='opponent_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nugget.Nug_IDs'),
        ),
    ]