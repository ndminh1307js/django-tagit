from django.urls import path

from .views import NewsFeedView, PostDetailView, PostLikeView, PostEditView, PostDeleteView

urlpatterns = [
    path('newsfeed/', NewsFeedView.as_view(), name='newsfeed'),
    path('<int:id>/', PostDetailView.as_view(), name='detail'),
    path('like/', PostLikeView.as_view(), name='like'),
    path('edit/<int:post_id>/', PostEditView.as_view(), name='post_edit'),
    path('delete/<int:post_id>/', PostDeleteView.as_view(), name='post_delete'),
]
