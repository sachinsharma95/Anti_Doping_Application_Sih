# Generated by Django 4.0.3 on 2022-08-08 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_filesupload_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filesupload',
            name='status',
            field=models.CharField(choices=[('Stage 1', 'Stage 1'), ('Stage 2', 'Stage 2'), ('Stage 3', 'Stage 3'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Stage 0', max_length=200, null=True),
        ),
    ]
