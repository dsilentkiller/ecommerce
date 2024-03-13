
from django.contrib import admin
from order.models import *
# Register your models here.
admin.site.register(OrderItem)
# # admin.site.register(FinalOrder)
admin.site.register(Payment)
admin.site.register(Refund)
admin.site.register(Address)
# admin.site.register(FinalOrder)
admin.site.register(Coupon)
admin.site.register(Order)
