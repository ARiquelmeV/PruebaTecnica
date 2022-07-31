from django.urls import path

from rest_framework import routers

from .views import ProductoViewSet

router = routers.DefaultRouter()
router.register('catalogo', ProductoViewSet)

urlpatterns = router.urls


