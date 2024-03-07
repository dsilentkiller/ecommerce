# Generated by Django 5.0.3 on 2024-03-07 02:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0004_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('ward_no', models.BigIntegerField()),
                ('tole_name', models.CharField(max_length=100)),
                ('landmark', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=200)),
                ('subtotal', models.FloatField()),
                ('created_at', models.DateField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='FinalOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.orderitem')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('payment_method', models.CharField(choices=[('Cash', 'Cash'), ('Fonepay', 'Fonepay'), ('Esewa', 'Esewa'), ('Bank', 'Bank')], max_length=100)),
                ('amount', models.FloatField()),
                ('final_order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.finalorder')),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipment_date', models.DateField()),
                ('final_oder_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.finalorder')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.payment')),
            ],
        ),
    ]