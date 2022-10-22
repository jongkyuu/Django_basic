from django.shortcuts import render

# Create your views here.

def regitster(request):
    return render(request, 'register.html')