from django.shortcuts import render
from . import models


def auto_view(request):
    if request.method == 'GET':
        cars = models.Car.objects.all().order_by('-id')
        context = {
            'cars': cars,

        }
    return render(
        request,
        template_name='cars.html',
        context=context
    )