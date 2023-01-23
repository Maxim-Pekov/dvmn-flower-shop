from .models import Bouquet, Order
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserForm, ConsultationForm
from yookassa import Payment, Configuration
from flowershop.settings import YOOKASSA_API_KEY, YOOKASSA_SHOP_ID


def index(request):
    bouquets = Bouquet.objects.all()

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
        context = {'form': form, 'bouquets': bouquets}
        return render(request, 'index.html', context)
    context = {
        'form': UserForm(),
        'bouquets': bouquets
    }
    return render(request, 'index.html', context)


def catalog_view(request):
    bouquets = Bouquet.objects.all()
    context = {
        'bouquets': bouquets
    }
    return render(request, 'catalog.html', context=context)


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
            'form': UserForm()
    }

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('result'))
        context['form'] = form
        return render(request, 'result.html', context)

    return render(request, 'result.html', context=context)


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
    context = {}
    if request.method == "POST":
        context['bouquet_title'] = request.POST['bouquet_title']
        context['bouquet_price'] = request.POST['bouquet_price']
        return render(request, 'order.html', context=context)
    return render(request, 'order.html', context=context)


def order_step_view(request):
    context = {}
    if request.method == "POST":
        order_number = save_order(request.POST)
        context['bouquet_title'] = request.POST['bouquet_title']
        context['bouquet_price'] = request.POST['bouquet_price']
        context['order_number'] = order_number
        return render(request, 'order-step.html', context=context)
    return render(request, 'order-step.html')


def recommend_bouquet(budget, occasion):
    return Bouquet.objects.order_by('?').first()


def card_view(request, card_id: int):
    bouquets = Bouquet.objects.filter(id=card_id)
    context = {
        'bouquet': bouquets[0],
        'form': UserForm(),
    }

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'card.html', context)
        context = {'form': form, 'bouquets': bouquets[0]}
        return render(request, 'index.html', context)

    context = {
        'bouquet': bouquets[0],
        'form': UserForm(),
    }
    return render(request, 'card.html', context)


def order_status_view(request, order_number: int):
    order = Order.objects.get(id=order_number)
    payment_id = order.payment_id

    Configuration.account_id = YOOKASSA_SHOP_ID
    Configuration.secret_key = YOOKASSA_API_KEY
    payment = Payment.find_one(payment_id)
    context = {
        'order_number': order_number,
        'message': payment.status,
    }
    return render(request, 'order_status.html', context)


def save_order(POST_dict):
    bouquet_name = POST_dict['bouquet_title']
    customer_name = POST_dict['name']
    customer_phone = POST_dict['phone']
    delivery_address = POST_dict['address']
    bouquet = Bouquet.objects.filter(title=bouquet_name).first()
    order = Order.objects.create(
        customer=customer_name,
        phone=customer_phone,
        address=delivery_address,
        bouquet=bouquet
    )
    return order.pk
