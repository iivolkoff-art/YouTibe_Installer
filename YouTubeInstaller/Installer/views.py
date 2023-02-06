from django.shortcuts import render

def index(request):
    return render(request, 'Installer/index.html')

def second_page(request):
    return render(request, 'Installer/install.html')
