from django.db import models

# Create your models here.
class Main(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description =models.TextField(
        verbose_name="Описание"
    )
    banner =models.ImageField(
        upload_to='banner/',
        verbose_name="Фото баннера"
    )
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name="Логотип"
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Настройки главной'
        verbose_name_plural = 'Настройки главной'

class Over(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    date = models.CharField(
        max_length=255,
        verbose_name="Год"
    )
    direction = models.CharField(
        max_length=255,
        verbose_name="Направление"
    )
    img = models.ImageField(
        upload_to='over/',
        verbose_name="Фото"
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Анимация'
        verbose_name_plural = 'Анимация'

class Awards(models.Model):
    image = models.ImageField(
        upload_to="awards/",
        verbose_name='Фото'
    )
    def __str__(self):
        return f"{self.image}"
    
    class Meta:
        verbose_name = "О нас (галарея)"
        verbose_name_plural = "О нас (галарея)"

class About(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    video = models.FileField(
        upload_to="video/",
        verbose_name='Видео'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"




