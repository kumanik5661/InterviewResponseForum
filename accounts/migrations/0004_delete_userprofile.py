# Generated by Django 3.0.4 on 2020-03-31 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200330_2221'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
