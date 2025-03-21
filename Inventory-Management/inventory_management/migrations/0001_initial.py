# Generated by Django 5.1.4 on 2025-01-07 15:17

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('food', 'FOOD'), ('kitchen', 'KITCHEN'), ('clothing', 'CLOTHING'), ('mobile', 'MOBILE'), ('computer', 'COMPUTER'), ('general', 'GENERAL')], max_length=20)),
                ('price', models.IntegerField(default=0)),
                ('stock', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('phone_number', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'PENDING'), ('completed', 'COMPLETED'), ('cancelled', 'CANCELLED')], max_length=15)),
                ('quantity', models.IntegerField(default=0)),
                ('total_price', models.IntegerField(default=0)),
                ('date', models.DateField(default=datetime.date(2025, 1, 7))),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_management.product')),
            ],
        ),
        migrations.CreateModel(
            name='Stock_Movement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movemet_type', models.CharField(choices=[('in', 'IN'), ('out', 'OUT')], max_length=5)),
                ('quantity', models.IntegerField(default=0)),
                ('date', models.DateField(default=datetime.date(2025, 1, 7))),
                ('note', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_management.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_management.supplier'),
        ),
    ]
