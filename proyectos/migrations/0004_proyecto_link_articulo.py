# Generated by Django 4.2.19 on 2025-03-03 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0003_alter_proyecto_fecha_publicacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='link_articulo',
            field=models.URLField(default=''),
        ),
    ]
