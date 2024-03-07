from django.contrib import admin
from orders.models import *
# Register your models here.
admin.site.register(OrderItem)
admin.site.register(FinalOrder)
admin.site.register(Payment)
admin.site.register(Shipment)
admin.site.register(Address)