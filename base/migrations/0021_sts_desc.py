# Generated by Django 3.0.5 on 2022-08-11 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_auto_20220810_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='sts',
            name='desc',
            field=models.TextField(default='Your Application is being Reviewed'),
        ),
    ]
