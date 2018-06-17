from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # ім`я лікаря, хто створює запис
    created_date = models.DateTimeField(  # дата внесення запмсу
        default=timezone.now)
    owner_first_name = models.CharField(max_length=50)  # ім`я госпордара тварини
    owner_last_name = models.CharField(max_length=50)  # прізвище господара тварини
    owner_phone_number = models.IntegerField  # телефон господара
    animal = models.CharField(max_length=50)  # тварина (пес, кіт, і т.д.)
    animal_name = models.CharField(max_length=50)  # кличка тварини
    disease = models.CharField(max_length=100)  # хвороба, діагноз, або причина візиту
    text = models.TextField()  # додаткові коментарі

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title