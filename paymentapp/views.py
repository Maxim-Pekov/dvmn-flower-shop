from django.shortcuts import render
from yookassa import Configuration, Payment
from flowershop.settings import YOOKASSA_API_KEY, YOOKASSA_SHOP_ID
from django.http import HttpResponse
from django.shortcuts import redirect


def make_payment(request):

    Configuration.account_id = '964811'
    Configuration.secret_key = 'test_6usWO5DsDOJZcaL9YN3eE7Ce9_GVUWj9-k7NPqo0A1A'

    payload = dict(request.POST.items())

    payment_token = payload.get('payment_token')
    amount = payload.get('price')
    description = payload.get('title')
    print(f'{amount= }')

    payment = Payment.create({
        "payment_token": payment_token,
        "amount": {
            "value": amount,
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "https://www.example.com/return_url"
        },
        "capture": False,
        "description": description
        }
    )
    print(payment.status)
    return HttpResponse('OKK')
