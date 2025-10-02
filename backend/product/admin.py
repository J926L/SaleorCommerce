# product 应用的 Django admin 配置

from django.contrib import admin
from .models import Category, Product, ProductType, ProductVariant, ProductImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """产品类别的 Admin 配置"""
    list_display = ('name', 'slug', 'parent')
    prepopulated_fields = {'slug': ('name',)}

class ProductImageInline(admin.TabularInline):
    """产品图片内联配置，用于在产品页面直接编辑图片"""
    model = ProductImage
    extra = 1 # 默认显示一个空的图片上传字段

class ProductVariantInline(admin.TabularInline):
    """产品变体内联配置，用于在产品页面直接编辑变体"""
    model = ProductVariant
    extra = 1 # 默认显示一个空的变体编辑字段

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """产品模型的 Admin 配置"""
    list_display = ('name', 'slug', 'product_type', 'category', 'is_published')
    list_filter = ('product_type', 'category', 'is_published')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline, ProductVariantInline]

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    """产品类型模型的 Admin 配置"""
    pass

@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    """产品变体模型的 Admin 配置"""
    list_display = ('product', 'sku', 'name', 'price', 'stock_quantity')
    list_filter = ('product',)

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    """产品图片模型的 Admin 配置"""
    list_display = ('product', 'alt_text', 'order')
    list_filter = ('product',)
