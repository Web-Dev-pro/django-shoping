from django.contrib import admin
from .models import Comment, Product, Category, ProductImage
# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','id','date','category','author']
    inlines = [ProductImageInline]


admin.site.register(Comment)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(ProductImage)
