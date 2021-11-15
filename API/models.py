from django.db import models

from django.db.models.deletion import CASCADE

# Create your models here.

class Destino(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre del destino', null= False, blank=False)
    image = models.ImageField(upload_to="destinos_img/", null= False, blank=False)
    description = models.TextField(verbose_name='Descripcion del Destino', null= False, blank=False)

    def __str__(self):
        return (self.name)

    class Meta:
        verbose_name_plural = 'Destinos'
        verbose_name = 'Destino'
        ordering = ['id']

class Empresa(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre de la Empresa', null= False, blank=False)
    logo = models.ImageField(upload_to='logo_empresas/', null=True, blank=True)
    phone = models.CharField(max_length=20, verbose_name='contacto de la Empresa', null= True, blank=True)
    email = models.EmailField(max_length=100, verbose_name='email de la Empresa', null= True, blank=True)

    def __str__(self):
        return (self.name)
    
    class Meta:
        verbose_name_plural = 'Empresas'
        verbose_name = 'Empresa'
        ordering = ['name']


class DestinosTuristicos(models.Model):
    destinos = models.ManyToManyField(Destino, verbose_name= "Seleccione los destinos")

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name_plural = 'Destinos Turisticos'
        verbose_name = 'Destino Turistico'
        ordering = ['id']

class Publicidad(models.Model):
    name = models.CharField(max_length=100, verbose_name='Publicidad', null=True, blank=True )
    image = models.ImageField(upload_to='img_publicidad/')
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'Publicidad'
        ordering = ['id']