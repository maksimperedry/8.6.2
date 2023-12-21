from django.urls import path
from . views import (
    NewsList, PostDetail, NewsSearch, PostCreate, PostEdit, PostDelete)
urlpatterns = [
    path('', NewsList.as_view(), name='news'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', NewsSearch.as_view(), name='search'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='delete')

    ]