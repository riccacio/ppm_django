# Generated by Django 5.0.6 on 2024-06-14 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollingAPI_app', '0004_choice_votes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Response',
        ),
    ]