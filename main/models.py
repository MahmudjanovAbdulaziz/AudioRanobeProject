from django.db import models


class Genre(models.Model):
    genres_tag = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.genres_tag} "


class RanobeTitle(models.Model):
    images = models.ImageField(upload_to='product' ,verbose_name="Изображение")
    title = models.CharField(max_length=180, verbose_name="Название")
    genres = models.ManyToManyField(Genre, verbose_name="Жанры")
    description = models.TextField(verbose_name="Описание")
    posted_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    like = models.IntegerField(default=0, verbose_name="Лайк (импровизированный)")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Рандомные произведения"
        verbose_name_plural = "Рандомные произведения"
