from django.db import models
from django.contrib.auth.models import User
from generales.models import TipoUsuario, Pais, Departamento, Municipio, InstitucionEducativa, Empresa

class InfoUsuario(models.Model):
    IdInfoUsuario = models.AutoField(primary_key=True, db_column='IdInfoUsuario')
    IdUsuario = models.OneToOneField(User, on_delete=models.CASCADE, db_column='IdUsuario')
    IdTipoUsuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE, db_column='IdTipoUsuario')
    IdPais = models.ForeignKey(Pais, on_delete=models.CASCADE, db_column='IdPais')
    IdDepartamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, db_column='IdDepartamento')
    IdMunicipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, db_column='IdMunicipio')
    IdInstitucionEducativa = models.ForeignKey(InstitucionEducativa, on_delete=models.CASCADE, db_column='IdInstitucionEducativa', default=1)
    IdEmpresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, db_column='IdEmpresa', default=1)
    CorreoInstitucional = models.CharField(max_length=250)
    Agnio = models.IntegerField()
    Telefono = models.CharField(max_length=20)
    FechaNacimiento = models.DateField()
    Carnet = models.CharField(max_length=100, null=True, blank=True)
    FotoPerfil = models.ImageField(upload_to='fotos-perfil/', null=True, blank=True)

    def __str__(self):
        return self.Nombre

    class Meta:
        db_table = 'InfoUsuario'
