from django.shortcuts import render

# Create your views here.

def catalog_view(request):
    return render(request, 'catalog.html')
