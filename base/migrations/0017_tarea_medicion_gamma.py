# Generated by Django 5.1.2 on 2024-12-06 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_anio_grupodetrabajo_remove_tarea_grupo_tarea_anio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='medicion_gamma',
            field=models.BooleanField(default=False),
        ),
    ]
