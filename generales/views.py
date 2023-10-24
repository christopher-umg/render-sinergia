from rest_framework import viewsets
from .models import Pais, Departamento, Municipio, SectorEmpresarial
from .serializers import PaisSerializer, DepartamentoSerializer, DepartamentoDetailSerializer, MunicipioSerializer, MunicipioDetailSerializer, SectorEmpresarialSerializer

class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'list':
            return DepartamentoDetailSerializer
        return DepartamentoSerializer

class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'list':
            return MunicipioDetailSerializer
        return MunicipioSerializer

class SectorEmpresarialViewSet(viewsets.ModelViewSet):
    queryset = SectorEmpresarial.objects.all()
    serializer_class = SectorEmpresarialSerializer