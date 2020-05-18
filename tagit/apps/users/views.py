from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, FormView
from django.conf import settings
from django.contrib import messages

from .forms import UserLoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile


class AuthenticationView(FormView):
    def post(self, request):
        form = UserLoginForm(request.POST)
        user_form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/users/edit')
                else:
                    return HttpResponse('Inactive user')
        elif user_form.is_valid():
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
