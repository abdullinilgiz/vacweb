from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Vacancy(models.Model):
    position = models.CharField(max_length=255)
    education = models.CharField(max_length=255, choices=[
        ('высшее', 'Высшее'),
        ('среднее', 'Среднее'),
        ('любое', 'Любое'),
    ])
    region = models.CharField(max_length=255, choices=[
        ('москва', 'Москва'),
        ('санкт-петербург', 'Санкт-Петербург'),
        ('московская-область', 'Московская область'),
        ('нижегородская-область', 'Нижегородская область'),
        ('краснодарский-край', 'Краснодарский край'),
    ])
    skills = models.TextField()
    schedule = models.CharField(max_length=255, choices=[
        ('полный-рабочий-день', 'Полный рабочий день'),
        ('сменный-график', 'Сменный график'),
        ('удаленная-работа', 'Удаленная работа'),
        ('свободный-график', 'Свободный график'),
        ('вахта', 'Вахта'),
        ('частичная-занятость', 'Частичная занятость'),
    ])
