from django_filters import FilterSet
from .models import News


# создаём фильтр
class NewsFilter(FilterSet):
    class Meta:
        model = News
        fields = {'news_create_time': ['lte'],
                  'news_text': ['icontains'],
                  'name': ['icontains'],
                  'category': ['exact'],
                  'news_author__author_user__username': ['icontains'],
                  }