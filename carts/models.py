from django.db import models
from store.models import Product, Variation
from accounts.models import Account


class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.cart_id


class CartItem(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    variations = models.ManyToManyField(Variation, blank=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.DO_NOTHING, null=True)
    quantity = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)

    def sub_total(self) -> float:
        return self.quantity * self.product.price

    def __str__(self) -> str:
        return self.product.product_name
