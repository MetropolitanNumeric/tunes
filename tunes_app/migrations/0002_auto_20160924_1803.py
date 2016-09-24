# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunes_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='track',
            old_name='album',
            new_name='albums',
        ),
    ]
