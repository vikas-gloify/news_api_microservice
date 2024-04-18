from django.urls import path

from main.fetch_news_api import FetchnewsView
from main.views import NewsView

urlpatterns = [
    path('finease_news',NewsView.as_view(), name='finease_news'),
    path('fetch_news', FetchnewsView.as_view(), name='fetch_news'),
]
