from django.db import models

# Create your models here.

class Consulta(models.Model):
    id_peticion = models.AutoField(primary_key=True) 
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Tipo_De_Documento = models.CharField(max_length=50)
    Numero_De_Documento = models.BigIntegerField()  # Cambiado a BigIntegerField
    Celular = models.CharField(max_length=20)
    Correo = models.EmailField()
    Servicio = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.Nombre} {self.Apellido}'