# Generated by Django 4.2.11 on 2024-03-17 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_alter_tripcomment_trip'),
    ]

    operations = [
        migrations.AddField(
            model_name='tripcomment',
            name='approved',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
