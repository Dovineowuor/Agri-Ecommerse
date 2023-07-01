from django.urls import path, include
from rest_framework import routers
from .views import (
    UserViewSet,
    ProductViewSet,
    CategoryViewSet,
    OrderViewSet,
    OrderItemViewSet,
    AddressViewSet,
    PaymentViewSet
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'payments', PaymentViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
