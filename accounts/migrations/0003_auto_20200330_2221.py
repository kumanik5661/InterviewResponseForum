# Generated by Django 3.0.4 on 2020-03-30 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200330_2145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employment',
            old_name='employer',
            new_name='company',
        ),
    ]
