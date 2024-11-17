# products/models.py

from django.db import models

class Product(models.Model):
    product_name = models.TextField(null=True)
    last_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    photo = models.ImageField(upload_to='products/', null=True, blank=True)
    note = models.TextField(null=True)
    note_photo = models.TextField(null=True)
    name = models.TextField(null=True)
    color = models.TextField(null=True)
    color_photo = models.TextField(null=True)
    size = models.TextField(null=True)
    size_photo = models.TextField(null=True)
    material = models.TextField(null=True)
    material_photo = models.TextField(null=True)
    description = models.TextField(null=True)
    description_photo = models.TextField(null=True)
    additional_info = models.TextField(null=True)
    additional_info_photo = models.TextField(null=True)
    additional_info_2 = models.TextField(null=True)
    additional_info_photo_2 = models.TextField(null=True)
    additional_info_3 = models.TextField(null=True)
    additional_info_photo_3 = models.TextField(null=True)
    packaging = models.TextField(null=True)
    packaging_photo = models.TextField(null=True)
    question = models.TextField(null=True)
    question_photo = models.TextField(null=True)
    defect_info = models.TextField(null=True)
    product_code = models.TextField(null=True)
    article = models.TextField(null=True, unique=True)
    factory_id = models.IntegerField(null=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.product_name
