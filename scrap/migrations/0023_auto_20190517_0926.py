# Generated by Django 2.2 on 2019-05-17 09:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0022_auto_20190517_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automationdata',
            name='entry_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 17, 9, 26, 43, 952910, tzinfo=utc)),
        ),
    ]
