from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm
from .models import User

class HomePageView(ListView):
    model = User
    template_name = 'index.html'

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,
               f'{username}, Your Account Has Been Created! You can login now!')
            return redirect('home') #change this route to login later
    else:
        form = UserRegisterForm()
    return render(request = request,
                  template_name = "accounts/register.html",
                  context={"form":form})
