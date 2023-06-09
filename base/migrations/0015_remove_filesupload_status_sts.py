# Generated by Django 4.0.3 on 2022-08-08 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0014_alter_filesupload_order_with_respect_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filesupload',
            name='status',
        ),
        migrations.CreateModel(
            name='Sts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Stage 1', 'Stage 1'), ('Stage 2', 'Stage 2'), ('Stage 3', 'Stage 3'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Stage 0', max_length=200, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
