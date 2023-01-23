from yookassa import Configuration, Payment
from flowershop.settings import YOOKASSA_API_KEY, YOOKASSA_SHOP_ID
from django.http import HttpResponse
from bucketorderapp.models import Order


def make_payment(request):

    Configuration.account_id = YOOKASSA_SHOP_ID
    Configuration.secret_key = YOOKASSA_API_KEY

    payload = dict(request.POST.items())

    payment_token = payload.get('payment_token')
    amount = payload.get('price')
    description = payload.get('title')

    order_number = payload.get('order_number')

    payment = Payment.create({
        "payment_token": payment_token,
        "amount": {
            "value": amount,
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": f"http://127.0.0.1:8000/order_status/{order_number}"
        },
        "capture": True,
        "description": description
        }
    )
    if payment.status == 'pending':
        order = Order.objects.get(id=order_number)
        order.payment_id = payment.id
        order.save()
        return HttpResponse(payment.confirmation.confirmation_url)
    else:
        print(payment.status)
        return HttpResponse('OK')
