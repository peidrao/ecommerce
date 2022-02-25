from django.shortcuts import render
from .forms import RegistartionForm

def register(request):
    context = {
        'form': RegistartionForm()
    }
    return render(request, 'accounts/register.html', context)

def login(request):
    return render(request, 'accounts/login.html', {})

def logout(request):
    pass
