from django.db import models

class Persona(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=8, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    domicilio = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.nombres, self.apellidos)
