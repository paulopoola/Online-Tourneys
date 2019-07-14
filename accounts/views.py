from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm, UserUpdateForm
from .models import User


class HomePageView(TemplateView):
    template_name = 'index.html'


class RegisterView(CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = UserCreationForm

#     def form_valid(self, request, *args, **kwargs):
#         username = form.cleaned_data.get('username')
#         messages.success(request,
#            f'{username}, Your Account Has Been Created! You can login now!')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # change this route to login later
    else:
        form = UserRegisterForm()
    return render(request=request,
                  template_name="accounts/register.html",
                  context={"form": form})
