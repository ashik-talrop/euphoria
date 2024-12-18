from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(
    upload_to='category/images', null=True, blank=True)

    class Meta:
        verbose_name = 'Category'  
        verbose_name_plural = 'Categories' 

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=2, unique=True)

    class Meta:
        verbose_name = 'Size'  
        verbose_name_plural = 'Sizes' 

    def __str__(self):
        return self.name

class Gender(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Gender'  
        verbose_name_plural = 'Genders' 

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    image = models.ImageField(
    upload_to='product/images', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ratings = models.PositiveIntegerField()
    comment_count = models.PositiveIntegerField()
    description = models.TextField()
    sizes = models.ManyToManyField(Size)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)  # New field

    class Meta:
        verbose_name = 'Product'  
        verbose_name_plural = 'Products' 

    def __str__(self):
        return self.name


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="User")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Wishlist'  
        verbose_name_plural = 'Wishlists'  

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name="customuser")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  # Added quantity field

    class Meta:
        unique_together = ('user', 'product')
        verbose_name = 'Cart Item'  
        verbose_name_plural = 'Cart Items'  

    def __str__(self):
        return f"{self.user.username}'s cart - {self.product.name} (x{self.quantity})"
