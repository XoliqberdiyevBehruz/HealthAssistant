# Generated by Django 4.2 on 2025-06-13 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0002_clinic_telegram_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='clinic',
            name='phone',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
    ]
