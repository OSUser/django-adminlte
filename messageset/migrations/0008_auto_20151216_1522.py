# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messageset', '0007_auto_20151216_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='content',
        ),
        migrations.AddField(
            model_name='notificationcontent',
            name='receivers',
            field=models.ManyToManyField(related_name='receivers', null=True, verbose_name='\u63a5\u6536\u4eba', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.RemoveField(
            model_name='notification',
            name='receiver',
        ),
        migrations.AddField(
            model_name='notification',
            name='receiver',
            field=models.ForeignKey(related_name='+', verbose_name='\u63a5\u6536\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]