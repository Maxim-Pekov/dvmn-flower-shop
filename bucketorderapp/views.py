from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def catalog_view(request):
    return render(request, 'catalog.html')

def quiz_view(request):
    return render(request, 'quiz.html')

def quiz_step_view(request):
    return render(request, 'quiz-step.html')

def result_view(request):
    return render(request, 'result.html')

def consultation_view(request):
    return render(request, 'consultation.html')

def order_view(request):
    return render(request, 'order.html')

def order_step_view(request):
    return render(request, 'order-step.html')
