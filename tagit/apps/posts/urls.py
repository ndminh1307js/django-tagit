from django.urls import path

from .views import NewsFeedView

urlpatterns = [
    path('newsfeed/', NewsFeedView.as_view(), name='newsfeed'),
]
