# Generated by Django 5.0.6 on 2024-06-11 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('l2pay', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apikey',
            name='enabled',
            field=models.BooleanField(db_index=True, default=True),
        ),
    ]
