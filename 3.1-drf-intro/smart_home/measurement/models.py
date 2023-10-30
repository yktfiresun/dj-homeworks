from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    description = models.CharField(max_length=100, verbose_name='Описание')

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, related_name='measurements', on_delete=models.CASCADE)
    temperature = models.FloatField(verbose_name='Температура измерения')
    created_at = models.DateField(auto_now=True,verbose_name='Дата и время измерения')