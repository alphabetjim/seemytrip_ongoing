# Generated by Django 4.2.11 on 2024-03-15 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripcomment',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tripcomments', to='trips.trip'),
        ),
    ]
