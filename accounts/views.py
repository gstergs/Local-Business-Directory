from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomLoginForm, CustomUserCreationForm
from .models import CustomUser

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = CustomLoginForm

class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
