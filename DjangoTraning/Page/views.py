from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Первая страница сайта")

def about (request):
    return HttpResponse("Страница about")