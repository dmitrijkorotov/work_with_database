from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone_objects = Phone.objects.all()
    phones_sort = request.GET.get('sort')
    if phones_sort == 'name':
        context = {'phones': [phone for phone in phone_objects.order_by('name')]}
    elif phones_sort == 'min_price':
        context = {'phones': [phone for phone in phone_objects.order_by('price')]}
    elif phones_sort == 'max_price':
        context = {'phones': [phone for phone in phone_objects.order_by('-price')]}
    else:
        context = {'phones': [phone for phone in phone_objects]}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug__contains=slug).first()
    context = {'phone': phone}
    return render(request, template, context)
