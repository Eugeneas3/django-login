from urllib import request
from django.shortcuts import render


def index(requests):
    return render(requests, 'index.html')

def djangologin(requests):
    pass
    