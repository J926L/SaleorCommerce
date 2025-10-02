# product 应用的 GraphQL schema 定义

import graphene
from graphene_django import DjangoObjectType
from .models import Category, Product, ProductType, ProductVariant, ProductImage

# 为 Category 模型创建 GraphQL 类型
class CategoryType(DjangoObjectType):
    """产品类别的 GraphQL 类型"""
    class Meta:
        model = Category
        fields = "__all__"

# 为 ProductType 模型创建 GraphQL 类型
class ProductTypeType(DjangoObjectType):
    """产品类型的 GraphQL 类型"""
    class Meta:
        model = ProductType
        fields = "__all__"

# 为 ProductImage 模型创建 GraphQL 类型
class ProductImageType(DjangoObjectType):
    """产品图片的 GraphQL 类型"""
    class Meta:
        model = ProductImage
        fields = "__all__"

# 为 ProductVariant 模型创建 GraphQL 类型
class ProductVariantType(DjangoObjectType):
    """产品变体的 GraphQL 类型"""
    class Meta:
        model = ProductVariant
        fields = "__all__"

# 为 Product 模型创建 GraphQL 类型
class ProductNode(DjangoObjectType):
    """产品的 GraphQL 类型"""
    class Meta:
        model = Product
        fields = "__all__"

# 定义产品相关的查询
class Query(graphene.ObjectType):
    """产品相关的根查询"""
    all_categories = graphene.List(CategoryType, description="获取所有产品类别")
    all_products = graphene.List(ProductNode, description="获取所有产品")
    product_by_slug = graphene.Field(ProductNode, slug=graphene.String(required=True), description="通过 slug 获取单个产品")

    def resolve_all_categories(self, info):
        """解析获取所有产品类别的请求"""
        return Category.objects.all()

    def resolve_all_products(self, info):
        """解析获取所有产品的请求"""
        return Product.objects.select_related('category', 'product_type').prefetch_related('variants', 'images').filter(is_published=True)

    def resolve_product_by_slug(self, info, slug):
        """解析通过 slug 获取单个产品的请求"""
        try:
            return Product.objects.select_related('category', 'product_type').prefetch_related('variants', 'images').get(slug=slug, is_published=True)
        except Product.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)
