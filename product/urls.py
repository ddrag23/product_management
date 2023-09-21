from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .model_views.product_views import ProductViewSet
router = DefaultRouter()
router.register(r'products', ProductViewSet)
urlpatterns = [
    path("", views.index, name="product"),
    path("add", views.store, name="product.store"),
    path("api/", include(router.urls))
]
