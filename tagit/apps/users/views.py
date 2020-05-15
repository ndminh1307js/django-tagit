from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.conf import settings

from .forms import UserLoginForm, UserRegistrationForm


class LoginView(View):
    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/newfeeds')
                else:
                    return HttpResponse('Inactive user')
            else:
                return HttpResponseRedirect(settings.REDIRECT_LOGIN_URL)
        return render(request, 'users/registration/login.html', {'form': form})

    def get(self, request):
        form = UserLoginForm()
        return render(request, 'users/registration/login.html', {'form': form})


class RegistrationView(View):
    def post(self, request):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new object but not saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the user object
            new_user.save()
            return render(request,
                          'users/registration/register_done.html',
                          {'new_user': new_user})

    def get(self, request):
        user_form = UserRegistrationForm()
        return render(request,
                      'users/registration/register.html',
                      {'user_form': user_form})
