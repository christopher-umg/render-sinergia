# Generated by Django 3.2 on 2023-10-28 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0007_alter_proyecto_autorescv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='AutoresCV',
            field=models.FileField(blank=True, null=True, upload_to='autores-cv/'),
        ),
    ]
