from django.db import models
from store.models import Product, Variation


class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.cart_id


class CartItem(models.Model):
    variations = models.ManyToManyField(Variation, blank=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    cart = models.ForeignKey(Cart, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)

    def sub_total(self) -> float:
        return self.quantity * self.product.price

    def __str__(self) -> str:
        return self.product.product_name
