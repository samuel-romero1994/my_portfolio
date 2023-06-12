from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=150, verbose_name="Título")#Campo para llenar sólo títulos
    descripction = models.TextField(max_length=1600, verbose_name="Descripción")#Campo más grande para descripciones con un máximo de caracteres
    image = models.ImageField(verbose_name="Imagen", upload_to='projects')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")#auto_now es para añadir fecha y hora
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")# se ejecuta cada que se actualiza una instancia

    #variable nueva:
    link = models.URLField(verbose_name="Enlace", null=True, blank=True)

    class Meta: #Subclase que establece el plural y singular en español, además de agregar el orden de aparición
        verbose_name='proyecto'
        verbose_name_plural='proyectos'
        ordering = ["-creation_date"]#la variable updated

    def __str__(self):
        return self.title#regresa el título del proyecto porque sin colocar esto
                         #me devuelve el atributo como: "Project object (1)"
