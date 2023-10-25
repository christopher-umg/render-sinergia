from rest_framework import viewsets
from rest_framework.response import Response
from .models import Pais, Departamento, Municipio, SectorEmpresarial
from .serializers import PaisSerializer, DepartamentoSerializer, MunicipioSerializer, SectorEmpresarialSerializer

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