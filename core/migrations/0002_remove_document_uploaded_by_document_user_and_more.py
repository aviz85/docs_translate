# Generated by Django 4.2.16 on 2024-10-23 01:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='uploaded_by',
        ),
        migrations.AddField(
            model_name='document',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='documents', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='source_language',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='document',
            name='target_language',
            field=models.CharField(max_length=10),
        ),
    ]
