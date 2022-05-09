from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    discount_price = models.FloatField()
    image = models.ImageField(upload_to='images')
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.title