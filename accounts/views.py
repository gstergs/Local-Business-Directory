from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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
    success_url = reverse_lazy('accounts:login')

@csrf_exempt
def ajax_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid credentials'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})
