from django.db import models
from django.contrib import admin

class Cliente(models.Model):
	id       = models.AutoField(primary_key=True)
	nombre   = models.CharField(max_length=25)
	telefono = models.CharField(max_length=25)
	email    = models.CharField(max_length=25)

	def __unicode__(self):
		return self.nombre

admin.site.register(Cliente)

class Plato(models.Model):
	id          = models.AutoField(primary_key=True)
	imagen      = models.ImageField(upload_to='imagenes')
	nombre      = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=500)
	valor       = models.CharField(max_length=25)	

	def __unicode__(self):
		return self.nombre

	def imagen_delete(instance):
	    """ Borra los ficheros de las fotos que se eliminan. """
	    instance.imagen.delete(False)
		
admin.site.register(Plato)





