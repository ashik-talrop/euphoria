from django.contrib import admin
from web.models import Product, Category, Gender, Size, Wishlist, Cart


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'brand', 'image', 'price', 'ratings',
                    'comment_count', 'description', 'category', 'gender']


class WishlistAdmin(admin.ModelAdmin):
    list_filter = ['user']  
    search_fields = ['user__username', 'product__name']


class CartAdmin(admin.ModelAdmin):
    list_filter = ['user']  


admin.site.register(Product, ProductAdmin)

admin.site.register(Category, CategoryAdmin)

admin.site.register(Gender)

admin.site.register(Size)

admin.site.register(Wishlist, WishlistAdmin)

admin.site.register(Cart, CartAdmin)
