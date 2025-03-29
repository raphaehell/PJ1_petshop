from django.shortcuts import render, redirect
from .models import Payment
from order.models import Order

def process_payment(request, order_id):
    order = Order.objects.get(id=order_id)
    payment = Payment.objects.create(order=order, amount=order.total_price, payment_method=request.POST.get('payment_method'))
    return redirect('payment_result', payment_id=payment.id)

def payment_result(request, payment_id):
    payment = Payment.objects.get(id=payment_id)
    return render(request, 'payment/payment.html', {'payment': payment})