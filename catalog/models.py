
from django.db import models

# Create your models here.
class Product(models.Model):
    GENDER_CHOICES = [
        ('M', 'Мужчина'),
        ('F', 'Женщина'),
    ]

    TYPE_CHOICES = [
        ('Шубы и меха', 'Шубы и меха'),
        ('Кожаные куртки', 'Кожаные куртки'),
        ('Плащи и тренчи', 'Плащи и тренчи'),
        ('Демисезонные куртки', 'Демисезонные куртки'),
        ('Пуховики и зимние куртки', 'Пуховики и зимние куртки'),
        ('Пальто', 'Пальто'),
        ('Шубы из овчины', 'Шубы из овчины'),
        ('Зимние кожаные куртки', 'Зимние кожаные куртки'),
        ('Дубленки', 'Дубленки'),
        ('Экошубы', 'Экошубы'),
        ('Сумки и рюкзаки', 'Сумки и рюкзаки'),
        ('Кошельки и обложки', 'Кошельки и обложки'),
        ('Платки и шарфы', 'Платки и шарфы'),
        ('Перчатки', 'Перчатки'),
        ('Головные уборы', 'Головные уборы'),
        ('Зонты', 'Зонты'),
        # ('Куртка', 'Куртка'),  # Сохраняем исходные типы для совместимости
        # ('Шуба', 'Шуба'),      # Сохраняем исходные типы для совместимости
        # ('Шапка', 'Шапка'),    # Сохраняем исходные типы для совместимости
    ]
    types = [
        ('Верхняя одежда', 'Верхняя одежда'),
        ('Аксессуар', 'Аксессуар')
    ]

    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    size = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    clothing_type = models.CharField(max_length=100, choices=TYPE_CHOICES, default=' ')
    type = models.CharField(max_length=100, choices=types ,default='Верхняя одежда')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
