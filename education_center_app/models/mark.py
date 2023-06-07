from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Mark(models.Model):

    mark = models.IntegerField("Оценка", validators=[MinValueValidator(1), MaxValueValidator(10)])
    date = models.DateTimeField("Дата")
    cource = models.ForeignKey("education_center_app.cource", on_delete=models.CASCADE, related_name="marks", 
                               verbose_name="Курс")
    student = models.ForeignKey("education_center_app.student", on_delete=models.CASCADE, related_name="marks", 
                               verbose_name="Студент")

    create_time = models.DateTimeField("Дата создания", auto_now_add=True)
    update_time = models.DateTimeField("Дата обновлени", auto_now=True)



