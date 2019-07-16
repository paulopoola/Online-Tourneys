"""
Online_Tourneys URL Configuration
"""
from django.contrib import admin
from django.urls import path
from accounts.views import HomePageView, RegisterView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(
       template_name='accounts/login.html'),
       name='login'),
    path('logout/', LogoutView.as_view(
      template_name='accounts/logout.html'),
      name='logout'),
    path('password-reset-confirm/<uidb64>/<token>',
      auth_views.PasswordResetConfirmView.as_view(
      template_name="accounts/password_reset_confirm.html"),
      name='password_reset_confirm'),
    path('password-reset-complete/',
      auth_views.PasswordResetCompleteView.as_view(
      template_name="accounts/password_reset_complete.html"),
      name='password_reset_complete'),
    path('password-reset/done',
      auth_views.PasswordResetDoneView.as_view(
      template_name="accounts/password_reset_done.html"),
      name='password_reset_done'),
    path('password-reset/',
      auth_views.PasswordResetView.as_view(
      template_name="accounts/password_reset.html"),
      name='password_reset'),
    path('', HomePageView.as_view(), name='home'),
]
