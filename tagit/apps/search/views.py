from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

from .forms import SearchForm
from tagit.apps.posts.models import Post


class SearchView(LoginRequiredMixin, View):
    template_name = 'search/search.html'

    def get(self, request):
        search_form = SearchForm()
        keyword = None
        user_results = []
        post_results = []

        if 'keyword' in request.GET:
            search_form = SearchForm(request.GET)
            if search_form.is_valid():
                keyword = search_form.cleaned_data['keyword']
                user_results = User.objects.filter(
                    Q(username__icontains=keyword) |
                    Q(first_name__icontains=keyword) |
                    Q(last_name__icontains=keyword)
                )
                print(user_results)
                post_results = Post.objects.filter(caption__icontains=keyword)
                print(post_results)

        return render(request,
                      self.template_name,
                      {'search_form': search_form,
                       'keyword': keyword,
                       'user_results': user_results,
                       'post_results': post_results})
