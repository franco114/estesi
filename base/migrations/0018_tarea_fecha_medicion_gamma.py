# Generated by Django 5.1.2 on 2024-12-06 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_tarea_medicion_gamma'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='fecha_medicion_gamma',
            field=models.DateField(blank=True, null=True),
        ),
    ]
