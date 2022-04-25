from django.utils import timezone
from django.db import models

# Create your models here.

class Client(models.Model):

    dni = models.IntegerField(verbose_name='DNI', primary_key=True, unique=True, blank=True)
    name = models.CharField(verbose_name='Nombres', max_length=50, blank=True, null=True)
    lastname = models.CharField(verbose_name='Apellidos', max_length=50, blank=True, null=True)
    age = models.IntegerField(verbose_name='Edad', blank=True, null=True)
    birthday = models.DateField(verbose_name='Fechas de nacimiento', blank=True, null=True)
    address = models.CharField(verbose_name='Direccion', max_length=100, blank=True, null=True)
    workplace = models.CharField(verbose_name='Lugar de trabajo', max_length=100, blank=True, null=True)
    phone = models.IntegerField(verbose_name='Celular', blank=True, null=True)
    date = models.DateField(verbose_name='Fecha', auto_now_add=True, blank=True, null=True)

    class Meta:

        verbose_name = 'Datos del cliente'
        verbose_name_plural = 'Datos de los clientes'
    
    def __str__(self) -> str:
        
        return str(self.dni)

class Treatment(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Cliente')
    reason = models.TextField(verbose_name='Motivo de la consulta', blank=True)
    allergies =  models.TextField(verbose_name='Alergias', blank=True)
    temp = models.CharField(verbose_name='Temperatura', max_length=20, blank=True)
    sat = models.CharField(verbose_name='Saturacion', max_length=20, blank=True)
    sick = models.TextField(verbose_name='Enfermedades presentes', blank=True)
    med = models.TextField(verbose_name='Medicacion actual', blank=True)
    treat = models.FileField(verbose_name='Tratamientos', upload_to='treatments/{year}/{month}/{day}/'.format(year= timezone.datetime.now().year, month= timezone.datetime.now().month, day= timezone.datetime.now().day))

    class Meta:

        verbose_name = 'Tratamiento'
        verbose_name_plural = 'Tratamientos'

    def __str__(self) -> str:
        
        return str(self.client)