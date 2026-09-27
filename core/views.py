from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenido a Core")
from django.shortcuts import redirect

def home_redirect_view(request):
    if request.user.is_authenticated:
        return redirect('accounts:dashboard')
    return redirect('accounts:login')