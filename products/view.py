# products/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.uploadhandler import FileUploadHandler
from django.core.exceptions import ValidationError
from .models import Product
from .form import ProductForm
import os
from django.conf import settings

def validate_image(image):
    # Проверка размера файла (максимум 5MB)
    max_size = 5 * 1024 * 1024  # 5MB
    if image.size > max_size:
        raise ValidationError('Размер файла не должен превышать 5MB')
    
    # Проверка расширения файла
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    ext = os.path.splitext(image.name)[1].lower()
    if ext not in valid_extensions:
        raise ValidationError('Поддерживаются только изображения (jpg, jpeg, png, gif)')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'list.html', {'products': products, 'MEDIA_URL': settings.MEDIA_URL})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'details.html', {'product': product})

def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Проверяем, есть ли файл в запросе
                if 'photo' in request.FILES:
                    photo = request.FILES['photo']
                    validate_image(photo)
                
                product = form.save(commit=False)
                
                # Если старое фото существует, удаляем его
                if product.photo and os.path.isfile(product.photo.path):
                    os.remove(product.photo.path)
                
                product.save()
                return redirect('product_list')
            except ValidationError as e:
                form.add_error('photo', e)
    else:
        form = ProductForm()
    return render(request, 'form.html', {'form': form})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            try:
                if 'photo' in request.FILES:
                    photo = request.FILES['photo']
                    validate_image(photo)
                    
                    # Если старое фото существует, удаляем его
                    if product.photo and os.path.isfile(product.photo.path):
                        os.remove(product.photo.path)
                    
                    # Сохраняем новое фото
                    product = form.save()
                else:
                    # Если новое фото не загружено, сохраняем форму без изменения фото
                    product = form.save(commit=False)
                    if product.photo:  # Сохраняем существующее фото
                        old_photo = Product.objects.get(pk=pk).photo
                        product.photo = old_photo
                    product.save()
                    
                return redirect('product_list')
            except ValidationError as e:
                form.add_error('photo', e)
    else:
        form = ProductForm(instance=product)
    return render(request, 'form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        # Удаляем фото при удалении продукта
        if product.photo and os.path.isfile(product.photo.path):
            os.remove(product.photo.path)
        product.delete()
        return redirect('product_list')
    return render(request, 'delete.html', {'product': product})
