# Generated by Django 4.0.5 on 2022-06-26 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptodo', '0002_remove_estado_categoria_delete_categoriadeestado'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='Clave',
            field=models.CharField(default='P', max_length=10),
        ),
    ]
