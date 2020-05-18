from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView

from .models import Post
from .forms import PostCreateForm


class NewsFeedView(LoginRequiredMixin, ListView):
    def post(self, request):
        print(request.POST)
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            # form data is valid
            cd = form.cleaned_data
            new_item = form.save(commit=False)

            # assign current user to the item
            new_item.user = request.user
            new_item.save()
            messages.success(request, "Post has been successfully created")
            return redirect(new_item.get_absolute_url())

    def get(self, request):
        form = PostCreateForm()
        posts = Post.objects.all()
        return render(request,
                      'posts/post/newsfeed.html',
                      {'posts': posts,
                       'form': form})


class PostDetailView(LoginRequiredMixin, DetailView):
    def get(self, request, id):
        post = get_object_or_404(Post, id=id)
        return render(request,
                      'posts/post/detail.html',
                      {'post': post})
