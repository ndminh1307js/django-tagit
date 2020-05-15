from django.urls import path
from django.contrib.auth import views as auth_views

from .views import LoginView

urlpatterns = [
    # Registration
    path('login/', LoginView.as_view(), name='login'),
    # Change password
    path('password_change/',
         auth_views.PasswordChangeView.as_view(
             template_name='users/registration/password_change_form.html'
         ),
         name='password_change'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='users/registration/password_change_done.html'
         ),
         name='password_change_done'),
    # Reset password
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/registration/password_reset_form.html'
         ),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/registration/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetView.as_view(
             template_name='users/registration/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetView.as_view(
             template_name='users/registration/password_reset_complete.html'
         ),
         name='password_reset_complete')
]
