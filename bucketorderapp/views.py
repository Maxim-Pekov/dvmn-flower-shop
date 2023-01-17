from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def catalog_view(request):
    return render(request, 'catalog.html')
