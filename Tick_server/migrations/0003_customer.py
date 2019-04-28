# Generated by Django 2.2 on 2019-04-18 19:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Tick_server', '0002_auto_20190419_0007'),
    ]

    operations = [
        migrations.CreateModel(
            name = 'Customer',
            fields = [
                ('id',
                 models.AutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'ID')),
                ('user',
                 models.OneToOneField(on_delete = django.db.models.deletion.CASCADE, to = settings.AUTH_USER_MODEL)),
            ],
        ),
    ]