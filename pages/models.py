from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=200)
    contenido = RichTextField(verbose_name="Contenido")
    orden = models.SmallIntegerField(verbose_name="Orden", default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_edicion = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['orden', 'titulo']

    def __str__(self):
        return self.titulo
