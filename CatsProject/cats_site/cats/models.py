from django.db import models
from django.urls import reverse

class TypeOfWool(models.Model):

    name = models.CharField("Тип шерсти", max_length=20)
    url = models.SlugField(max_length=160, unique = True)

    class Meta:
        verbose_name = "Тип шерсти"
        verbose_name_plural = "Тип шерсти"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("middleware", kwargs={"slug":self.url})

class Life_style(models.Model):

    name = models.CharField("Образ жизни", max_length=100)

    class Meta:
        verbose_name = "Образ жизни"
        verbose_name_plural = "Образ жизни"

    def __str__(self):
        return self.name

class Care(models.Model):

    name = models.CharField("Уход", max_length=100)

    class Meta:
        verbose_name = "Уход"
        verbose_name_plural = "Уход"

    def __str__(self):
        return self.name

class Attachment(models.Model):

    name = models.CharField("Привязанность", max_length=100)

    class Meta:
        verbose_name = "Привязанность"
        verbose_name_plural = "Привязанность"

    def __str__(self):
        return self.name

class Activity(models.Model):

    name = models.CharField("Активность", max_length=100)

    class Meta:
        verbose_name = "Активность"
        verbose_name_plural = "Активность"

    def __str__(self):
        return self.name

class Sociability(models.Model):

    name = models.CharField("Общительность", max_length=100)

    class Meta:
        verbose_name = "Общительность"
        verbose_name_plural = "Общительность"

    def __str__(self):
        return self.name

class Noisiness(models.Model):

    name = models.CharField("Разговорчивость", max_length=100)

    class Meta:
        verbose_name = "Разговорчивость"
        verbose_name_plural = "Разговорчивость"

    def __str__(self):
        return self.name

class Characteristics(models.Model):

    life_style = models.ForeignKey(Life_style, verbose_name="Образ жизни", on_delete=models.CASCADE)
    care = models.ForeignKey(Care, verbose_name="Уход", on_delete=models.CASCADE)
    attachment = models.ForeignKey(Attachment, verbose_name="Привязанность", on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, verbose_name="Активность", on_delete=models.CASCADE)
    sociability = models.ForeignKey(Sociability, verbose_name="Общительность", on_delete=models.CASCADE)
    noisiness = models.ForeignKey(Noisiness, verbose_name="Разговорчивость", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Характеристики"
        verbose_name_plural = "Характеристики"

class Cat(models.Model):

    type_of_wool = models.ForeignKey(TypeOfWool, verbose_name="Тип шерсти", on_delete=models.CASCADE)
    name = models.CharField("Порода", max_length=100)
    height = models.CharField("Рост", max_length=100)
    weight = models.CharField("Вес", max_length=100)
    health = models.CharField("Здоровье", max_length=250)
    life_span = models.CharField("Продолжительность жизни", max_length=100)
    country_of_origin = models.CharField("Страна происхождения", max_length=50)
    characteristics = models.ManyToManyField(Characteristics, verbose_name="Характеристики")
    about = models.CharField("О породе", max_length=1000)
    lifestyle = models.CharField("Образ жизни", max_length=1000)
    qualities = models.CharField("Качества", max_length=500)
    img = models.ImageField("Изображение", upload_to="image/")
    img_for_list = models.ImageField("Изображение 2", upload_to="image/", default=img)
    url = models.SlugField(max_length=160, unique = True)
    style = models.CharField("Стиль для списка", max_length=100, default='example1 example2')
    image_style = models.CharField("Стиль отображения картинки", max_length=100, default='e-photo')
    text_style = models.CharField("Стиль отбражения текста", max_length=100, default='e-ph-text')

    class Meta:
        verbose_name = "Кот"
        verbose_name_plural = "Кот"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("middleware", kwargs={"slug":self.url})