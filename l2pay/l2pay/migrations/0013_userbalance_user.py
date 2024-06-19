# Generated by Django 5.0.6 on 2024-06-14 07:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('l2pay', '0012_userbalance_alter_payments_state'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='userbalance',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='balances', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]