from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet, OrderItemViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('orders', OrderViewSet)
router.register('items', OrderItemViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('auth/login/', TokenObtainPairView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),
]