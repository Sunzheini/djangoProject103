import random

from django.http import HttpResponse
from django.shortcuts import render


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Name: {self.name}; Age: {self.age}"


def index(request):
    context = {
        'title': 'SoftUni Homepage',
        'value': random.random(),
        'info': {'address': 'Sofia'},
        'student': Student('Daniel', 40),
    }
    return render(request, 'index.html', context)






