from django.forms import ModelForm
from .models import News

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['news_author', 'news_text', 'name', 'category' ]