from django.shortcuts import render


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

    # TODO  отображение букета по параметрам из запроса, передача его в order/

    return render(request, 'result.html')


def consultation_view(request):
    return render(request, 'consultation.html')


def order_view(request):
    return render(request, 'order.html')


def order_step_view(request):
    return render(request, 'order-step.html')
