# product 应用的模型定义

from django.db import models

class Category(models.Model):
    """产品类别模型"""
    name = models.CharField(max_length=255, verbose_name="类别名称")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL Slug")
    description = models.TextField(blank=True, null=True, verbose_name="类别描述")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name="父类别")

    class Meta:
        verbose_name = "产品类别"
        verbose_name_plural = "产品类别"

    def __str__(self):
        return self.name

class ProductType(models.Model):
    """产品类型模型，用于定义产品的属性（例如，服装的尺寸和颜色）"""
    name = models.CharField(max_length=255, verbose_name="产品类型名称")

    class Meta:
        verbose_name = "产品类型"
        verbose_name_plural = "产品类型"

    def __str__(self):
        return self.name

class Product(models.Model):
    """产品模型"""
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='products', verbose_name="产品类型")
    name = models.CharField(max_length=255, verbose_name="产品名称")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL Slug")
    description = models.TextField(blank=True, null=True, verbose_name="产品描述")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products', verbose_name="产品类别")
    is_digital = models.BooleanField(default=False, verbose_name="是否为数字产品")
    is_published = models.BooleanField(default=True, verbose_name="是否发布")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "产品"
        verbose_name_plural = "产品"

    def __str__(self):
        return self.name

class ProductVariant(models.Model):
    """产品变体模型（例如，一件T恤的S码，红色）"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants', verbose_name="所属产品")
    sku = models.CharField(max_length=255, unique=True, verbose_name="库存单位 (SKU)")
    name = models.CharField(max_length=255, blank=True, verbose_name="变体名称")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="价格")
    stock_quantity = models.IntegerField(default=0, verbose_name="库存数量")

    class Meta:
        verbose_name = "产品变体"
        verbose_name_plural = "产品变体"

    def __str__(self):
        return self.name or self.sku

class ProductImage(models.Model):
    """产品图片模型"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name="所属产品")
    image = models.ImageField(upload_to='products/', verbose_name="图片文件")
    alt_text = models.CharField(max_length=255, blank=True, verbose_name="替代文本")
    order = models.PositiveIntegerField(default=0, verbose_name="显示顺序")

    class Meta:
        verbose_name = "产品图片"
        verbose_name_plural = "产品图片"
        ordering = ['order']
