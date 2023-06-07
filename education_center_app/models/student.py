from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Student(models.Model):

    first_name = models.CharField("Имя", max_length=200)
    last_name = models.CharField("Фамилия", max_length=200)
    email = models.EmailField("Email", max_length=200)
    create_time = models.DateTimeField("Дата создания", auto_now_add=True)
    update_time = models.DateTimeField("Дата обновлени", auto_now=True)

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self) -> str:
        return self.first_name + " " +  self.last_name

