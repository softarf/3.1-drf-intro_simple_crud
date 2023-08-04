from django.db import models


class Project(models.Model):
    """ 'Датчик' - Прибор, производящий измерения на объекте. """

    name = models.TextField(verbose_name='Название', unique=True)         # location or model & inventory number
    latitude = models.FloatField(verbose_name='Широта')      # -90 < x <= 90
    longitude = models.FloatField(verbose_name='Долгота')    # -180 < x <= 180
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    #
    objects = models.Manager()      # Диспетчер записей.

    class Meta:
        verbose_name = 'Термодатчик'
        verbose_name_plural = 'Термодатчики'
        ordering = ['id']
        unique_together = ('latitude', 'longitude')

    def __str__(self):
        return self.name


class Measurement(models.Model):
    """ 'Замер' - Измерение температуры на объекте. """

    value = models.FloatField(verbose_name='Температура')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='measurements')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    #
    objects = models.Manager()      # Диспетчер записей.

    class Meta:
        verbose_name = 'Замер'
        verbose_name_plural = 'Замеры'
        ordering = ['-created_at', ]

    def __str__(self):
        return f'{self.project}: {self.created_at} - {self.value} `C'
