from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_id = models.AutoField()
    product_category = models.CharField(max_length=255)
    product_description = models.CharField(max_length=255)
    product_image_url = models.CharField(max_length=255)
    product_price = models.IntegerField()

    def __str__(self):
        return str(self.title)