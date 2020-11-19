from django.db import models


class Order(models.Model):
    product = models.CharField(max_length=100, verbose_name='product')
    created_datetime = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.product
