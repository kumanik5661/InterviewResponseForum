# Generated by Django 3.0.4 on 2020-03-13 07:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('responseForum', '0010_responseview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responseview',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
