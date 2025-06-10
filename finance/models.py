from django.db import models
from django.contrib.auth.models import User

class Shipment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tracking_number = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    shipment_date = models.DateField()
    delivery_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.tracking_number} ({self.user.username})"
    
class Refund(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.TextField()
    refund_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Refund {self.id} for {self.shipment.tracking_number}"
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100)

    def __str__(self):
        return f"Payment {self.transaction_id}"

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Wallet"
    
class FXTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_currency = models.CharField(max_length=10)
    converted_currency = models.CharField(max_length=10)
    original_amount = models.DecimalField(max_digits=10, decimal_places=2)
    converted_amount = models.DecimalField(max_digits=10, decimal_places=2)
    fx_rate = models.FloatField()
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"FXTransaction {self.id} - {self.original_currency} to {self.converted_currency}"
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username