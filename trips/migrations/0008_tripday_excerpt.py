# Generated by Django 4.2.11 on 2024-03-21 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0007_tripday_locations'),
    ]

    operations = [
        migrations.AddField(
            model_name='tripday',
            name='excerpt',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
