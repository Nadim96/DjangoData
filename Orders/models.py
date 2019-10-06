from django.db import models
import datetime


class OrderInfo(models.Model):
    order_name = models.CharField(max_length=255, blank=True)
    order_description = models.CharField(max_length=255, blank=True)
    order_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    order_amount = models.PositiveSmallIntegerField(default=1, blank=True)
    order_date = models.DateField(default=datetime.date.today, blank=True)

    def __str__(self):
        return self.order_name
