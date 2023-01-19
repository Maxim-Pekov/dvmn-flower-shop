from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserForm, ConsultationForm


def index(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
        context = {'form': form}
        return render(request, 'index.html', context)
    context = {'form': UserForm()}
    return render(request, 'index.html', context)


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

    if request.method == "POST":
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('consultation'))
        context = {'form': form}
        return render(request, 'consultation.html', context)
    context = {'form': ConsultationForm()}
    return render(request, 'consultation.html', context)


def order_view(request):
    return render(request, 'order.html')


def order_step_view(request):
    return render(request, 'order-step.html')
