from django.db import models
from shop.models import Product, Pricing
from userauth.models import CustomUser

# Create your models here.
class CartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    item_price = models.IntegerField(null=True)
    plan_name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(default=1, null=True)
    item_paid = models.BooleanField(default=False)
    
    def __str__(self):
        return self.plan_name

    class Meta:
        db_table = 'cartitem'
        managed = True
        verbose_name = 'CartItem'
        verbose_name_plural = 'CartItems'