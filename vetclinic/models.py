from django.db import models
from django.utils import timezone


class Clinic(models.Model):
    clinic_name = models.CharField(max_length=30)  # назва клініки

    def __str__(self):
        return self.clinic_name


class User(models.Model):
    owner_full_name = models.CharField(max_length=70)  # ім`я госпордара тварини
    owner_phone_number = models.CharField(max_length=14, unique=True)  # телефон господара

    def __str__(self):
        return self.owner_full_name


class Animal(models.Model):
    owner_full_name = models.ForeignKey(User, on_delete=models.CASCADE)
    animal = models.CharField(max_length=50)  # тварина (пес, кіт, і т.д.)
    animal_name = models.CharField(max_length=20)  # кличка тварини
    animal_birth_date = models.DateField()  # дата народження тварини

    def __str__(self):
        return self.animal_name


class Record(models.Model):
    clinic_name = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    owner_full_name = models.ForeignKey(User, on_delete=models.CASCADE)
    animal_name = models.ForeignKey(Animal, on_delete=models.CASCADE)
    disease = models.CharField(max_length=100)  # хвороба, діагноз, або причина візиту
    text = models.TextField()  # додаткові коментарі
    visit_date = models.DateTimeField(  # дата відвідування клініки
        default=timezone.now)

    def __str__(self):
        return self.disease

    def publish(self):
        self.published_date = timezone.now()
        self.save()
