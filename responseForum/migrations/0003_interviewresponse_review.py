# Generated by Django 3.0.4 on 2020-03-07 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('responseForum', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviewresponse',
            name='review',
            field=models.CharField(max_length=1000000, null=True),
        ),
    ]
