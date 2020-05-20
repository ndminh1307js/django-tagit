import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import View, FormView
from django.conf import settings
from django.contrib import messages

from .forms import UserLoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile, Contact

from ..posts.models import Post


class AuthenticationView(FormView):
    def post(self, request):
        formname = request.POST.get('formname')

        if formname == 'login':
            form = UserLoginForm(request.POST)

            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(request,
                                    username=cd['username'],
                                    password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('/posts/newsfeed/')
                    else:
                        return HttpResponse('Inactive user')
                else:
                    HttpResponse('Invalid user login')

        if formname == 'register':
            user_form = UserRegistrationForm(request.POST)

            if user_form.is_valid():
                # Create a new object but not saving it yet
                new_user = user_form.save(commit=False)
                # Set the chosen password
                new_user.set_password(user_form.cleaned_data['password'])
                # Save the user object
                new_user.save()
                Profile.objects.create(user=new_user)

            return render(request,
                          'users/registration/register_done.html',
                          {'new_user': new_user})

    def get(self, request):
        form = UserLoginForm()
        user_form = UserRegistrationForm()
        return render(request,
                      'users/registration/auth.html',
                      {'user_form': user_form,
                       'form': form})


class UserEditView(LoginRequiredMixin, FormView):
    template_name = 'users/profile/edit.html'

    def post(self, request):
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')

        return render(request,
                      self.template_name,
                      {'user_form': user_form,
                       'profile_form': profile_form})

    def get(self, request):
        user_form = UserEditForm(instance=request.user)
        try:
            profile_form = ProfileEditForm(instance=request.user.profile)
        except:
            profile_form = ProfileEditForm()

        return render(request,
                      self.template_name,
                      {'user_form': user_form,
                       'profile_form': profile_form})


class UserProfileView(LoginRequiredMixin, View):
    template_name = 'users/profile/profile.html'

    def get(self, request, user_id):
        user = get_object_or_404(User,
                                 id=user_id)
        posts = Post.objects.filter(user=user)
        return render(request,
                      self.template_name,
                      {'user': user,
                       'posts': posts})


class UserFollowView(LoginRequiredMixin, View):
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        user_id = data.get('id')
        action = data.get('action')
        if user_id and action:
            try:
                user = User.objects.get(id=user_id)
                if action == 'follow':
                    Contact.objects.get_or_create(user_from=request.user,
                                                  user_to=user)
                else:
                    Contact.objects.filter(user_from=request.user,
                                           user_to=user).delete()
                return JsonResponse({'status': 'ok'})
            except User.DoesNotExist:
                return JsonResponse({'status': 'error'})
        return JsonResponse({'status': 'error'})
