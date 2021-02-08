from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Role:
    MANUFACTURER = "MANUFACTURER"
    DISTRIBUTER = "DISTRIBUTER"
    RESELLER = "RESELLER"

    CHOICES = (
        (MANUFACTURER, "Manufacturer"),
        (DISTRIBUTER, "Distributer"),
        (RESELLER, "Reseller"),
    )

class Seller(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(choices=Role.CHOICES, default=Role.MANUFACTURER, max_length=50)
    parent = models.ForeignKey("Seller", null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Inventory(models.Model):
    product = models.ForeignKey("Product", null=True, blank=True, on_delete=models.CASCADE)
    seller = models.ForeignKey("Seller", on_delete=models.CASCADE)
    price = models.PositiveIntegerField()

    class Meta:
        unique_together = ["product", "seller"]


    def __str__(self):
        return f"{self.product} - {self.seller} - {self.price}"

