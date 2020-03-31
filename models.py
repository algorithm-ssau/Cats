from django.db import models

# Create your models here.
class Category(models.Model):
    #Категории
    Nowool=models.TextField("Бесшерстные")
    Shortwool=models.TextField("Короткошерстные")
    Longwool=models.TextField("Длинношерстные")

    def __str__(self):
        return super().__str__()
    
    class Meta:
        verbose_name="Категория"
        verbose_name_plural="Категории"

class WoolType(models.Model):
    #Типшерсти
    Nowool=models.TextField("Бесшерстная")
    Shortwool=models.TextField("Короткая")
    Longwool=models.TextField("Длинная")

    def __str__(self):
        return super().__str__()

    class Meta:
        verbose_name="Тип шерсти"
        verbose_name_plural="Типы шерсти"

class Size(models.Model):
    #Размер
    Small=models.TextField("Маленькие")
    Middle=models.TextField("Средние")
    Big=models.TextField("Большие")

    def __str__(self):
        return super().__str__()

    class Meta:
        verbose_name="Размер"
        verbose_name_plural="Размеры"

class LifeStyle(models.Model):
    #Образжизни
    Home=models.TextField("В помещении")
    Street=models.TextField("На улице\В помещении")

    def __str__(self):
        return super().__str__()

    class Meta:
        verbose_name="Образ жизни"
        verbose_name_plural="Образ жизни"

class Qualities(models.Model):
    #Качества
    Affective=models.TextField("Ласковая")
    Independent=models.TextField("Независимая")
    Calm=models.TextField("Спокойная")
    Hyperactive=models.TextField("Гиперактивная")
    Sociable=models.TextField("Общительная")
    Closed=models.TextField("Замкнутая")
    Silent=models.TextField("Молчаливая")
    Talkative=models.TextField("Разговорчивая")

    def __str__(self):
        return super().__str__()

    class Meta:
        verbose_name="Качества"
        verbose_name_plural="Качества"

class Cat(models.Model):
    #Коты
    breedname=models.CharField("Название породы", max_length=1000)
    lifestyle=models.ForeignKey(LifeStyle, verbose_name="Образ жизни", on_delete=models.CASCADE)
    character=models.CharField("Характер", max_length=3000)
    wooltype=models.ForeignKey(WoolType, verbose_name="Тип шерсти", on_delete=models.CASCADE)
    size=models.ForeignKey(Size,verbose_name="Размер", on_delete=models.CASCADE)
    health=models.CharField("Здоровье", max_length=3000)
    qualities=models.ForeignKey(Qualities, verbose_name="Качества", on_delete=models.CASCADE)
    photo=models.ImageField("Изображение", upload_to="photocats/")
    country=models.TextField("Страна", max_length=1000)
    lifelong=models.CharField("Продолжительность жизни", max_length=10)

    def __str__(self):
        return super().__str__()

    class Meta:
        verbose_name="Кот"
        verbose_name_plural="Коты"

class Reviews(models.Model):
    #Отзывы
    email=models.EmailField()
    name=models.CharField("Имя", max_length=100)
    text=models.TextField("Сообщение", max_length=5000)
    parent=models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    cat=models.ForeignKey(Cat, verbose_name="кот", on_delete=models.CASCADE)

    def __str__(self):
        return super().__str__()

    class Meta:
        verbose_name="Отзыв"
        verbose_name_plural="Отзывы"