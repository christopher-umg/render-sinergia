from django.urls import path, include
from rest_framework import routers
from .views import PaisViewSet, DepartamentoViewSet, MunicipioViewSet, SectorEmpresarialViewSet, TipoUsuarioViewSet, TipoActividadUsuarioViewSet, MonedaViewSet, CategoriasEmpleosViewSet, CategoriaProyectosViewSet

router = routers.DefaultRouter()
router.register(r'paises', PaisViewSet)
router.register(r'departamentos', DepartamentoViewSet)
router.register(r'municipios', MunicipioViewSet)
router.register(r'sectores-empresariales', SectorEmpresarialViewSet)
router.register(r'tipo-usuarios', TipoUsuarioViewSet)
router.register(r'tipo-actividad-usuarios', TipoActividadUsuarioViewSet)
router.register(r'monedas', MonedaViewSet)
router.register(r'categorias-empleos', CategoriasEmpleosViewSet)
router.register(r'categorias-proyectos', CategoriaProyectosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
