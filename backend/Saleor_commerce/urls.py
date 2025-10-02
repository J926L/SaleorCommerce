# Saleor_commerce 的 URL 配置

from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # GraphQL 端点，我们使用 csrf_exempt 来允许外部客户端（如店面）进行 POST 请求
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('', RedirectView.as_view(url='/graphql/')),
]
