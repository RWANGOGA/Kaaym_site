# Generated by Django 5.2.3 on 2025-06-27 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_teammember'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='whatsapp_link',
        ),
        migrations.AddField(
            model_name='teammember',
            name='phone',
            field=models.CharField(blank=True, help_text='Phone number in international format (e.g., +1234567890)', max_length=15),
        ),
        migrations.AddField(
            model_name='teammember',
            name='whatsapp',
            field=models.CharField(blank=True, help_text='WhatsApp number in international format (e.g., +1234567890)', max_length=15),
        ),
    ]
