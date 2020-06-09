from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    barcode = models.CharField(
        db_index=True,
        unique=True,
        max_length=100,
        primary_key=True,
    )
    price_piece = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name
