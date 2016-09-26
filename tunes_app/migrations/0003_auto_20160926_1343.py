# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunes_app', '0002_auto_20160924_1803'),
    ]

    operations = [
        migrations.RenameField(
            model_name='track',
            old_name='albums',
            new_name='album',
        ),
    ]
