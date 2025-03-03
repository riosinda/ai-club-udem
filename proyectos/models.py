from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class FotoAutor(models.Model):
    # Relación uno-a-muchos: un autor puede tener varias fotos
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='fotos')
    foto = models.ImageField(upload_to='autores/')

    def __str__(self):
        return f"Foto de {self.autor.nombre}"

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()

    # Foto (una) del producto
    foto_producto = models.ImageField(
    upload_to='productos/', 
    default='productos/default.svg'
    )

    # Link del producto (URL)
    link_producto = models.URLField(default='')

    # Link del Articulo (DOI)
    link_articulo = models.URLField(default='')

    # Relación muchos-a-muchos con Autor: varios autores pueden participar
    autores = models.ManyToManyField(Autor)

    # Fecha de publicación automática
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.titulo
