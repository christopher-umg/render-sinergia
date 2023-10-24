from rest_framework import serializers
from .models import Pais, Departamento, Municipio, SectorEmpresarial

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = '__all__'

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class DepartamentoDetailSerializer(serializers.ModelSerializer):
    IdPais = PaisSerializer()
    class Meta:
        model = Departamento
        fields = '__all__'

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'

class MunicipioDetailSerializer(serializers.ModelSerializer):
    IdDepartamento = DepartamentoSerializer()
    class Meta:
        model = Municipio
        fields = '__all__'

class SectorEmpresarialSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectorEmpresarial
        fields = '__all__'