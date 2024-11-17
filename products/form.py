# products/forms.py

from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'last_price', 'photo', 'note', 'note_photo', 'name', 
                  'color', 'color_photo', 'size', 'size_photo', 'material', 
                  'material_photo', 'description', 'description_photo', 
                  'additional_info', 'additional_info_photo', 
                  'additional_info_2', 'additional_info_photo_2', 
                  'additional_info_3', 'additional_info_photo_3', 
                  'packaging', 'packaging_photo', 'question', 
                  'question_photo', 'defect_info', 'product_code', 
                  'article', 'factory_id']
