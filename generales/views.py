from rest_framework import viewsets
from rest_framework.response import Response
from .models import Pais, Departamento, Municipio, SectorEmpresarial, TipoUsuario, TipoActividadUsuario, Moneda, CategoriasEmpleos, CategoriaProyectos
from .serializers import PaisSerializer, DepartamentoSerializer, MunicipioSerializer, SectorEmpresarialSerializer, TipoUsuarioSerializer, TipoActividadUsuarioSerializer, MonedaSerializer, CategoriasEmpleosSerializer, CategoriaProyectosSerializer

class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        departamentos = Departamento.objects.filter(IdPais=instance)
        departamentos_serializer = DepartamentoSerializer(departamentos, many=True)
        data = serializer.data
        data['Departamentos'] = departamentos_serializer.data
        return Response(data)

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        municipios = Municipio.objects.filter(IdDepartamento=instance)
        municipios_serializer = MunicipioSerializer(municipios, many=True)
        data = serializer.data
        data['Municipios'] = municipios_serializer.data
        return Response(data)

class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer

class SectorEmpresarialViewSet(viewsets.ModelViewSet):
    queryset = SectorEmpresarial.objects.all()
    serializer_class = SectorEmpresarialSerializer

class TipoUsuarioViewSet(viewsets.ModelViewSet):
    queryset = TipoUsuario.objects.all()
    serializer_class = TipoUsuarioSerializer

class TipoActividadUsuarioViewSet(viewsets.ModelViewSet):
    queryset = TipoActividadUsuario.objects.all()
    serializer_class = TipoActividadUsuarioSerializer

class MonedaViewSet(viewsets.ModelViewSet):
    queryset = Moneda.objects.all()
    serializer_class = MonedaSerializer

class CategoriasEmpleosViewSet(viewsets.ModelViewSet):
    queryset = CategoriasEmpleos.objects.all()
    serializer_class = CategoriasEmpleosSerializer

class CategoriaProyectosViewSet(viewsets.ModelViewSet):
    queryset = CategoriaProyectos.objects.all()
    serializer_class = CategoriaProyectosSerializer