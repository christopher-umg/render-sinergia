# Generated by Django 3.2 on 2023-10-26 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generales', '0005_categoriaproyectos'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstitucionEducativa',
            fields=[
                ('IdInstitucionEducativa', models.AutoField(db_column='IdInstitucionEducativa', primary_key=True, serialize=False)),
                ('Universidad', models.BooleanField()),
                ('Nombre', models.CharField(max_length=250)),
                ('Descripcion', models.TextField()),
                ('Foto', models.ImageField(blank=True, null=True, upload_to='instituciones/fotos/')),
                ('IdDepartamento', models.ForeignKey(db_column='IdDepartamento', on_delete=django.db.models.deletion.CASCADE, to='generales.departamento')),
                ('IdMunicipio', models.ForeignKey(db_column='IdMunicipio', on_delete=django.db.models.deletion.CASCADE, to='generales.municipio')),
                ('IdPais', models.ForeignKey(db_column='IdPais', on_delete=django.db.models.deletion.CASCADE, to='generales.pais')),
            ],
            options={
                'db_table': 'InstitucionEducativa',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('IdEmpresa', models.AutoField(db_column='IdEmpresa', primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=250)),
                ('Descripcion', models.TextField()),
                ('Foto', models.ImageField(blank=True, null=True, upload_to='empresas/fotos/')),
                ('IdDepartamento', models.ForeignKey(db_column='IdDepartamento', on_delete=django.db.models.deletion.CASCADE, to='generales.departamento')),
                ('IdMunicipio', models.ForeignKey(db_column='IdMunicipio', on_delete=django.db.models.deletion.CASCADE, to='generales.municipio')),
                ('IdPais', models.ForeignKey(db_column='IdPais', on_delete=django.db.models.deletion.CASCADE, to='generales.pais')),
                ('IdSectorEmpresarial', models.ForeignKey(db_column='IdSectorEmpresarial', on_delete=django.db.models.deletion.CASCADE, to='generales.sectorempresarial')),
            ],
            options={
                'db_table': 'Empresa',
            },
        ),
    ]