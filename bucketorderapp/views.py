from django.shortcuts import render
from .models import Bouquet


def index(request):
    return render(request, 'index.html')


def catalog_view(request):
    return render(request, 'catalog.html')


def quiz_view(request):
    return render(request, 'quiz.html')


def quiz_step_view(request):
    payload = dict(request.POST.items())
    occasion = payload.get('occasion')
    context = {
        'occasion': occasion
    }
    return render(request, 'quiz-step.html', context=context)


def result_view(request):
    payload = dict(request.POST.items())
    budget = payload.get('budget')
    occasion = payload.get('occasion')

    bouquet = recommend_bouquet(budget, occasion)
    if bouquet is None:
        bouquet = {}
        bouquet['title'] = 'Милорд, база букетов пуста'
        bouquet['price'] = 0
        flowers = None
    else:
        flowers = bouquet.flowers.all()
    context = {
            'bouquet': bouquet,
            'flowers': flowers,
    }

    return render(request, 'result.html', context=context)


def consultation_view(request):
    return render(request, 'consultation.html')


def order_view(request):
    return render(request, 'order.html')


def order_step_view(request):
    return render(request, 'order-step.html')


def recommend_bouquet(budget, occasion):
    return Bouquet.objects.first()
