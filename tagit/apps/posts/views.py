import json

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView, View, FormView
from django.urls import reverse

from .models import Post
from .forms import PostCreateForm, CommentCreateForm

from tagit.apps.actions.utils import create_action


class NewsFeedView(LoginRequiredMixin, ListView):
    def post(self, request):
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            # form data is valid
            cd = form.cleaned_data
            new_item = form.save(commit=False)

            # assign current user to the item
            new_item.user = request.user
            new_item.save()
            create_action(request.user, 'added', new_item)
            messages.success(request, "Post has been successfully created")
            return redirect(new_item.get_absolute_url())

    def get(self, request):
        form = PostCreateForm()
        posts = Post.objects.all()
        following_ids = request.user.following.values_list('id', flat=True)

        if following_ids:
            posts = posts.filter(user_id__in=following_ids)

        return render(request,
                      'posts/post/newsfeed.html',
                      {'posts': posts,
                       'form': form})


class PostDetailView(LoginRequiredMixin, DetailView):
    def post(self, request, id):
        comment_form = CommentCreateForm(request.POST)
        if comment_form.is_valid():
            # form data is valid
            cd = comment_form.cleaned_data
            new_comment = comment_form.save(commit=False)

            # assign current user to the new comment
            new_comment.user = request.user
            # assign current post to the new comment
            post = get_object_or_404(Post, id=id)
            new_comment.post = post

            new_comment.save()
            create_action(request.user, 'added', new_comment)
            messages.success(
                request, "Your comment has been successfully sent")
            return redirect(f'/posts/{id}')

    def get(self, request, id):
        comment_form = CommentCreateForm()
        post = get_object_or_404(Post, id=id)
        return render(request,
                      'posts/post/detail.html',
                      {'post': post,
                       'comment_form': comment_form})


class PostLikeView(LoginRequiredMixin, View):
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        post_id = data.get('id')
        action = data.get('action')
        if post_id and action:
            try:
                post = Post.objects.get(id=post_id)
                if action == 'like':
                    post.users_like.add(request.user)
                    create_action(request.user, 'liked', post)
                else:
                    post.users_like.remove(request.user)
                return JsonResponse({'status': 'ok'})
            except:
                pass
        return JsonResponse({'status': 'error'})


class PostEditView(LoginRequiredMixin, FormView):
    template_name = 'posts/post/edit.html'

    def post(self, request, post_id):
        post = Post.objects.get(id=post_id, user__id=request.user.id)
        post_form = PostCreateForm(instance=post,
                                   data=request.POST,
                                   files=request.FILES)
        if post_form.is_valid():
            post_form.save()
            create_action(request.user, 'has just editted', post)
            messages.success(request, 'Post has been successfully editted')
        else:
            messages.error(request, 'Post editting has been failed')

        return redirect(f'/posts/{post_id}/')

    def get(self, request, post_id):
        post = Post.objects.get(id=post_id, user__id=request.user.id)
        post_form = PostCreateForm(instance=post)

        return render(request,
                      self.template_name,
                      {'post_form': post_form})


class PostDeleteView(LoginRequiredMixin, View):
    def post(self, request, post_id):
        post = Post.objects.get(id=post_id, user__id=request.user.id)
        post.delete()
        return JsonResponse({'status': 'ok'})

    def get(self, request, post_id):
        post = Post.objects.get(id=post_id, user__id=request.user.id)
        return render(request,
                      'posts/post/delete.html',
                      {'post': post})
