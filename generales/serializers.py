from rest_framework import serializers
from .models import Pais, Departamento, Municipio, SectorEmpresarial, TipoUsuario, TipoActividadUsuario, Moneda, CategoriasEmpleos, CategoriaProyectos

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = '__all__'

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'

class SectorEmpresarialSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectorEmpresarial
        fields = '__all__'

class TipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUsuario
        fields = '__all__'

class TipoActividadUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoActividadUsuario
        fields = '__all__'

class MonedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moneda
        fields = '__all__'

class CategoriasEmpleosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriasEmpleos
        fields = '__all__'

class CategoriaProyectosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProyectos
        fields = '__all__'