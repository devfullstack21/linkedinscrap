# Generated by Django 2.2 on 2019-05-17 08:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0018_auto_20190517_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automationdata',
            name='entry_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 17, 8, 29, 21, 905731)),
        ),
    ]