# Generated by Django 3.2 on 2023-10-27 02:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generales', '0008_rename_nombres_sectorempresarial_nombre'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('IdProyecto', models.AutoField(db_column='IdProyecto', primary_key=True, serialize=False)),
                ('Titulo', models.CharField(max_length=250)),
                ('Descripcion', models.TextField()),
                ('FechaPublicacion', models.DateTimeField()),
                ('AutoresCV', models.FileField(blank=True, null=True, upload_to='autores-cv/')),
                ('DocAceptacion', models.FileField(blank=True, null=True, upload_to='documentos-aceptacion/')),
                ('DocClasificacion', models.FileField(blank=True, null=True, upload_to='documentos-clasificacion/')),
                ('DocTipificacion', models.FileField(blank=True, null=True, upload_to='documentos-tipificacion/')),
                ('DocIdentificacion', models.FileField(blank=True, null=True, upload_to='documentos-identificacion/')),
                ('AvalEducativo', models.FileField(blank=True, null=True, upload_to='avales-educativo/')),
                ('BriefProyecto', models.FileField(blank=True, null=True, upload_to='brief-proyectos/')),
                ('LienzoCanva', models.FileField(blank=True, null=True, upload_to='lienzos-canva/')),
                ('DocAPA', models.FileField(blank=True, null=True, upload_to='documentos-apa/')),
                ('ProFinanciera', models.FileField(blank=True, null=True, upload_to='documentos-financieros/')),
                ('Presentacion', models.FileField(blank=True, null=True, upload_to='presentaciones/')),
                ('Video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('IdCategoriaProyecto', models.ForeignKey(db_column='IdCategoriaProyecto', on_delete=django.db.models.deletion.CASCADE, to='generales.categoriaproyectos')),
                ('IdUsuario', models.ForeignKey(db_column='IdUsuario', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Proyecto',
            },
        ),
    ]
