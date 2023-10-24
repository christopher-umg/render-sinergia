from django.urls import path, include
from rest_framework import routers
from .views import PaisViewSet, DepartamentoViewSet, MunicipioViewSet, SectorEmpresarialViewSet

router = routers.DefaultRouter()
router.register(r'paises', PaisViewSet)
router.register(r'departamentos', DepartamentoViewSet)
router.register(r'municipios', MunicipioViewSet)
router.register(r'sectores-empresariales', SectorEmpresarialViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
