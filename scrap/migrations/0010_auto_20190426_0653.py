# Generated by Django 2.2 on 2019-04-26 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0009_auto_20190426_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automationdata',
            name='status',
            field=models.BooleanField(),
        ),
    ]
