from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm, UserUpdateForm
from .models import User


class HomePageView(TemplateView):
    template_name = 'index.html'


class RegisterView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    success_message =' Your Account Has Been Created!, Activate your account now!'
