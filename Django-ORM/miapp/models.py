from django.db import models

# Create your models here.
# https://atharvashah.netlify.app/posts/tech/django-orm-exercises/

class Turno(models.Model):
    nombre = models.CharField(max_length=50)
    servicio = models.CharField(max_length=50)
    
