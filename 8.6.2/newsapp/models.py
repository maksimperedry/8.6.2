from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator

class Author(models.Model):
    author_user = models.OneToOneField(User, on_delete = models.CASCADE)
    author_rate = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.author_user}'


#  создаём категорию, к которой будет привязываться новость
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name.title()}'


# Создаём модель новость
class News(models.Model):
    news_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    news_create_time = models.DateTimeField(auto_now_add=True)
    news_text = models.TextField(default="None")
    name = models.CharField( max_length=100, unique=True)

    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='all_news',
    )

    def __str__(self):
        return f'{self.name.title()}: {self.news_text[:50]}  {self.news_create_time} '

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу новости
        return f'/news/{self.id}'


class NewsCategory(models.Model):
    news_temp = models.ForeignKey(News, on_delete=models.CASCADE)
    category_temp = models.ForeignKey(Category, on_delete=models.CASCADE)