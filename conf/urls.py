"""
Online_Tourneys URL Configuration
"""
from django.contrib import admin
from django.urls import path
# from accounts import views as user_views
from accounts.views import HomePageView, RegisterView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('', HomePageView.as_view(), name='home'),
]
