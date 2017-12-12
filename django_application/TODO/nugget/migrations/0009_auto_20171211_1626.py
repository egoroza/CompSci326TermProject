# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-11 21:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('nugget', '0008_auto_20171211_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this forum post', primary_key=True, serialize=False, verbose_name='forum id')),
                ('user1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chat_user_1', to='nugget.Profile', verbose_name='User1 in the chat')),
                ('user2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chat_user_2', to='nugget.Profile', verbose_name='User2 in the chat')),
            ],
            options={
                'ordering': ['id', 'user1', 'user2'],
            },
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, default='None', help_text='message content', max_length=200, verbose_name='content')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Post Date')),
                ('chatThread', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nugget.Chat', verbose_name='link to the chat thread')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nugget.Profile', verbose_name='User in the chat corresponding to this message')),
            ],
            options={
                'ordering': ['chatThread', 'user', 'content', 'date'],
            },
        ),
        migrations.RemoveField(
            model_name='forum',
            name='user',
        ),
        migrations.RemoveField(
            model_name='forumcomments',
            name='originalPost',
        ),
        migrations.RemoveField(
            model_name='forumcomments',
            name='user',
        ),
        migrations.DeleteModel(
            name='Forum',
        ),
        migrations.DeleteModel(
            name='ForumComments',
        ),
    ]