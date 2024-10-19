# Generated by Django 5.0.6 on 2024-07-20 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_product_clothing_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('Шубы и меха', 'Шубы и меха'), ('Кожаные куртки', 'Кожаные куртки'), ('Плащи и тренчи', 'Плащи и тренчи'), ('Демисезонные куртки', 'Демисезонные куртки'), ('Пуховики и зимние куртки', 'Пуховики и зимние куртки'), ('Пальто', 'Пальто'), ('Шубы из овчины', 'Шубы из овчины'), ('Зимние кожаные куртки', 'Зимние кожаные куртки'), ('Дубленки', 'Дубленки'), ('Экошубы', 'Экошубы'), ('Сумки и рюкзаки', 'Сумки и рюкзаки'), ('Кошельки и обложки', 'Кошельки и обложки'), ('Платки и шарфы', 'Платки и шарфы'), ('Перчатки', 'Перчатки'), ('Головные уборы', 'Головные уборы'), ('Зонты', 'Зонты')], default='Верхняя одежда', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='clothing_type',
            field=models.CharField(choices=[('Шубы и меха', 'Шубы и меха'), ('Кожаные куртки', 'Кожаные куртки'), ('Плащи и тренчи', 'Плащи и тренчи'), ('Демисезонные куртки', 'Демисезонные куртки'), ('Пуховики и зимние куртки', 'Пуховики и зимние куртки'), ('Пальто', 'Пальто'), ('Шубы из овчины', 'Шубы из овчины'), ('Зимние кожаные куртки', 'Зимние кожаные куртки'), ('Дубленки', 'Дубленки'), ('Экошубы', 'Экошубы'), ('Сумки и рюкзаки', 'Сумки и рюкзаки'), ('Кошельки и обложки', 'Кошельки и обложки'), ('Платки и шарфы', 'Платки и шарфы'), ('Перчатки', 'Перчатки'), ('Головные уборы', 'Головные уборы'), ('Зонты', 'Зонты')], default='Куртка', max_length=100),
        ),
    ]