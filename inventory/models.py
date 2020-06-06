from django.db import models

class Product(models.Model):
    serial_number = models.CharField(
        db_index=True,
        unique=True,
        max_length=100
    )
    name = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    price_p_p = models.FloatField(blank=True)

    def __str__(self):
        return self.name
