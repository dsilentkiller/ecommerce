from django.db import models
from product.models import Product

# Create your models here.
METHOD = (('Cash', 'Cash'),
          ('Fonepay', 'Fonepay'),
          ('Esewa', 'Esewa'),
          ('Bank', 'Bank'))


class OrderItem(models.Model):
    quantity = models.CharField(max_length=200)
    subtotal = models.FloatField()
    created_at = models.DateField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.subtotal


class FinalOrder(models.Model):
    order_item_id = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    # payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)


class Payment(models.Model):
    name = models.CharField(max_length=300)
    final_order_id = models.ForeignKey(FinalOrder, on_delete=models.CASCADE)
    payment_method = models.CharField(choices=METHOD, max_length=100)
    amount = models.FloatField()

    def __str__(self):
        return self.name


class Shipment(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    final_oder_id = models.ForeignKey(FinalOrder, on_delete=models.CASCADE)
    shipment_date = models.DateField()

    # def __str__(self):
    #     return  f'{orders.payment}-{orders.shipment_date}'


class Address(models.Model):
    city = models.CharField(max_length=100)
    ward_no = models.BigIntegerField()
    tole_name = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)

    def __str__(self):
        return self.city
