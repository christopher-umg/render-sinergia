from django.db import models

class Pais(models.Model):
    IdPais = models.AutoField(primary_key=True, db_column='IdPais')
    NombreCorto = models.CharField(max_length=10)
    Nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.Nombre

    class Meta:
        db_table = 'Pais'

class Departamento(models.Model):
    IdDepartamento = models.AutoField(primary_key=True, db_column='IdDepartamento')
    NombreCorto = models.CharField(max_length=10)
    Nombre = models.CharField(max_length=250)
    IdPais = models.ForeignKey(Pais, on_delete=models.CASCADE, db_column='IdPais')

    def __str__(self):
        return self.Nombre

    class Meta:
        db_table = 'Departamento'

class Municipio(models.Model):
    IdMunicipio = models.AutoField(primary_key=True, db_column='IdMunicipio')
    NombreCorto = models.CharField(max_length=10)
    Nombre = models.CharField(max_length=250)
    IdDepartamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, db_column='IdDepartamento')

    def __str__(self):
        return self.Nombre

    class Meta:
        db_table = 'Municipio'
