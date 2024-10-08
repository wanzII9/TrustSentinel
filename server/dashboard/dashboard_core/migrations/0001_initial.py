# Generated by Django 5.1.1 on 2024-09-11 22:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PLCList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plc_id', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SlaveDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slave_id', models.IntegerField()),
                ('slave_vendor', models.CharField(max_length=255)),
                ('slave_product', models.CharField(max_length=255)),
                ('slave_version', models.CharField(max_length=255)),
                ('product_id', models.CharField(max_length=255)),
                ('slave_temp', models.FloatField(default=0)),
                ('slave_status', models.BooleanField(default=False)),
                ('plc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard_core.plclist')),
            ],
        ),
    ]
