from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # Registration
    path('auth/', views.AuthenticationView.as_view(), name='auth'),
    path('logout/',
         auth_views.LogoutView.as_view(
             template_name='users/registration/logout.html'
         ),
         name='logout'),
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
         name='password_reset_complete'),
    # Edit user profile
    path('edit/', views.UserEditView.as_view(), name='edit'),
    # Profile
    path('profile/<int:user_id>/',
         views.UserProfileView.as_view(),
         name='profile'),
    # Follow
    path('follow/', views.UserFollowView.as_view(), name='follow'),
    # Activities
    path('activities/', views.UserActivitiesView.as_view(), name='activities'),
]
