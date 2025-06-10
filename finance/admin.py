from django.contrib import admin
from .models import Shipment, Refund, Payment, Wallet, FXTransaction

admin.site.register(Shipment)
admin.site.register(Refund)
admin.site.register(Payment)
admin.site.register(Wallet)
admin.site.register(FXTransaction)

# Register your models here.
