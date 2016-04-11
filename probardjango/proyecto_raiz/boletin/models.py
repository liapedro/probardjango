from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Registrado(models.Model):
	nombre = models.CharField(max_length = 120, blank = False, null = False) 
	email = models.EmailField()
	codigo_postal = models.IntegerField(blank = True, null = True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	actualizado = models.DateTimeField(auto_now_add = False, auto_now = True)	
	latitud = models.CharField(max_length = 20, blank = False, null = False)
	longitud = models.CharField(max_length = 20, blank = False, null = False)

	def __unicode__(self): #En Python se utiliza __str__
		return self.email