# Generated by Django 5.0.6 on 2024-06-13 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('l2pay', '0010_alter_payments_fee_asset_alter_payments_net_asset_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network', models.CharField(db_index=True, max_length=20)),
                ('symbol', models.CharField(db_index=True, max_length=20)),
                ('contract_address', models.CharField(db_index=True, max_length=100)),
                ('block_hash', models.CharField(db_index=True, max_length=100)),
                ('block_number', models.BigIntegerField(db_index=True)),
                ('block_timestamp', models.DateTimeField(db_index=True)),
                ('transaction_hash', models.CharField(db_index=True, max_length=150)),
                ('transfer_id', models.CharField(db_index=True, max_length=150)),
                ('from_address', models.CharField(db_index=True, max_length=150)),
                ('to_address', models.CharField(db_index=True, max_length=150)),
                ('amount', models.DecimalField(db_index=True, decimal_places=18, max_digits=50)),
                ('amount_raw', models.TextField()),
                ('_cursor', models.BigIntegerField()),
            ],
            options={
                'db_table': 'transfers',
                'managed': False,
            },
        ),
    ]
