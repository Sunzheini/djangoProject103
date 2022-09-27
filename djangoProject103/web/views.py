import random

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'SoftUni Homepage',
        'value': random.random(),
        'info': {'address': 'Sofia'},
    }
    return render(request, 'index.html', context)

