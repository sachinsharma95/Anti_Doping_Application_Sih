# Generated by Django 4.0.3 on 2022-08-08 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_news_geeks_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilesUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
