from django.db import models
class Employee(models.Model):
    fabricante = models.CharField(max_length=20,default='')
    categoria = models.CharField(max_length=100,default='')
    indi_carga = models.CharField(max_length=5,default='')
    indi_velocidad = models.CharField(max_length=15,default='')
    lonas = models.CharField(max_length=15,default='')
    eancho = models.CharField(max_length=15,default='')
    perfil = models.CharField(max_length=15,default='')
    rin = models.CharField(max_length=15,default='')
    class Meta:
        db_table = "employee"