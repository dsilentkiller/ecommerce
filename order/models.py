from django.db import models

# Create your models here.
from django.db import models
from product.models import Product

# Create your models here.
METHOD = (('Cash', 'Cash'),
          ('Fonepay', 'Fonepay'),
          ('Esewa', 'Esewa'),
          ('Bank', 'Bank'))

ADDRESS_CHOICES = (('B', 'Billing'),
                   ('S', 'Shipping'))


class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=30)
    payment_method = models.CharField(choices=METHOD, max_length=100)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.stripe_charge_id


class Address(models.Model):
    country = models.CharField(max_length=30, default=False, null=True)
    municipality = models.CharField(max_length=50, default=False, null=True)
    city = models.CharField(max_length=100, default=False, null=True)
    ward_no = models.BigIntegerField()
    tole_name = models.CharField(max_length=100, default=False, null=True)
    landmark = models.CharField(max_length=100, default=False, null=True)
    address_type = models.CharField(
        choices=ADDRESS_CHOICES, default=False)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name_plural = 'Addresses'


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code


class OrderItem(models.Model):
    quantity = models.CharField(max_length=200)
    subtotal = models.FloatField()
    created_at = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    def get_total_item_price(self):
        return self.quantity * self.product.price

    def get_total_discount_item_price(self):
        return self.quantity * self.product.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.product.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    ref_code = models.CharField(max_length=20, null=True)
    product = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        'Address', related_name='shipping_address', on_delete=models.CASCADE, blank=True)
    billing_address = models.ForeignKey(
        Address, related_name='billing_address', on_delete=models.CASCADE, blank=True)
    payment = models.ForeignKey(
        Payment, on_delete=models.CASCADE, blank=True, null=True)
    coupon = models.ForeignKey(
        Coupon, on_delete=models.CASCADE, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)

    def __str__(self):
        return self.ref_code

    def get_total(self):
        total = 0

        for order_item in self.product.all():
            total += order_item.get_final_price()

        if self.coupon:
            total -= self.coupon.amount
        return total


class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.pk}"


# def userprofile_receiver(sender,instance,created,*args,**kwargs):
#         if created:
#             userprofile =UserProfile.objects.create(user=instance)
#          post_save.connect(userprofile_receiver,sender=settings.AUTH__USER_MODEL)
# class FinalOrder(models.Model):
#     order_item_id = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
#     # payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)


# class Shipment(models.Model):
#     payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
#     final_oder_id = models.ForeignKey(FinalOrder, on_delete=models.CASCADE)
#     shipment_date = models.DateField()

        '''
            1. Item added to cart
            2. Adding a billing address
            (Failed checkout)
            3. Payment
            (Preprocessing, processing, packaging etc.)
            4. Being delivered
            5. Received
            6. Refunds
            '''
