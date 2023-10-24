from django.contrib import admin
from .models import Pais, Departamento, Municipio, SectorEmpresarial

admin.site.register(Pais)
admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(SectorEmpresarial)
