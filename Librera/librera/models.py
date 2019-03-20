from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    class Meta:
        ordering = ('id',)

class Libro(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=100)
    editorial = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=5,decimal_places=2)
    def __str__(self):
        return self.nombre
    class Meta:
        ordering = ('id',)

