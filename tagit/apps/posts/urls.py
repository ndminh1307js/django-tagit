from django.urls import path

from .views import NewsFeedView, PostDetailView

urlpatterns = [
    path('newsfeed/', NewsFeedView.as_view(), name='newsfeed'),
    path('<int:id>/', PostDetailView.as_view(), name='detail')
]
