# Generated by Django 2.2 on 2019-04-25 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0006_automationdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='automations',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='scrap.LinkedIn'),
        ),
    ]
