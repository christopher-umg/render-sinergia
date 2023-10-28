from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Pais, Departamento, Municipio, SectorEmpresarial, TipoUsuario, TipoActividadUsuario, Moneda, CategoriasEmpleos, CategoriaProyectos, Empresa, InstitucionEducativa
from Login.models import Proyecto, PostulacionEmpleo
from .serializers import PaisSerializer, DepartamentoSerializer, MunicipioSerializer, SectorEmpresarialSerializer, TipoUsuarioSerializer, TipoActividadUsuarioSerializer, MonedaSerializer, CategoriasEmpleosSerializer, CategoriaProyectosSerializer, EmpresaSerializer, InstitucionEducativaSerializer, ProyectoSerializer, PostulacionEmpleoSerializer

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
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = SectorEmpresarial.objects.all()
    serializer_class = SectorEmpresarialSerializer

class TipoUsuarioViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = TipoUsuario.objects.all()
    serializer_class = TipoUsuarioSerializer

class TipoActividadUsuarioViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = TipoActividadUsuario.objects.all()
    serializer_class = TipoActividadUsuarioSerializer

class MonedaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Moneda.objects.all()
    serializer_class = MonedaSerializer

class CategoriasEmpleosViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CategoriasEmpleos.objects.all()
    serializer_class = CategoriasEmpleosSerializer

class CategoriaProyectosViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CategoriaProyectos.objects.all()
    serializer_class = CategoriaProyectosSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class InstitucionEducativaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = InstitucionEducativa.objects.all()
    serializer_class = InstitucionEducativaSerializer

class ProyectoViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Proyecto.objects.filter(IdProyecto=0)
    serializer_class = ProyectoSerializer

class PostulacionEmpleoViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PostulacionEmpleo.objects.filter(IdPostulacionEmpleo=0)
    serializer_class = PostulacionEmpleoSerializer