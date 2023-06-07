from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Cource(models.Model):

    name = models.CharField("Название", max_length=200)
    description = models.CharField("Описание", max_length=200)
    duration = models.IntegerField("Длительность")
    create_time = models.DateTimeField("Дата создания", auto_now_add=True)
    update_time = models.DateTimeField("Дата обновлени", auto_now=True)
    
    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self) -> str:
        return self.name

