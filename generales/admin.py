from django.contrib import admin
from .models import Pais, Departamento, Municipio, SectorEmpresarial, TipoUsuario, TipoActividadUsuario, Moneda, CategoriasEmpleos, CategoriaProyectos

admin.site.register(Pais)
admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(SectorEmpresarial)
admin.site.register(TipoUsuario)
admin.site.register(TipoActividadUsuario)
admin.site.register(Moneda)
admin.site.register(CategoriasEmpleos)
admin.site.register(CategoriaProyectos)
