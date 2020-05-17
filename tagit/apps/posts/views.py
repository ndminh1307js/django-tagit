from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView

from .models import Post
from .forms import PostCreateForm


class NewsFeedView(ListView):
    def get(self, request):
        posts = Post.objects.all()
        return render(request,
                      'posts/post/newsfeed.html',
                      {'posts': posts})
