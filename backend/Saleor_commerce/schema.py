# GraphQL Schema 定义

import graphene
import product.schema

# 定义一个根查询，它继承了所有应用级别的查询
class Query(product.schema.Query, graphene.ObjectType):
    """根查询对象"""
    # 这里可以保留根级别的查询，或者将其移动到单独的应用中
    pass

# 创建 schema
schema = graphene.Schema(query=Query)
