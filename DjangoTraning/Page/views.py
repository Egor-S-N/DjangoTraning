from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseNotFound,Http404
# Create your views here.
def index(request):
    return HttpResponse("Первая страница сайта")

def about (request):
    return HttpResponse("Страница about")

def getValue(request, id):
    if (id > 12):
        raise Http404()
    elif (id < 5):
        return redirect("/about", permanent=False)
    return HttpResponse(f"<h1>Your id is: {id}</h1>")

def pageNotFound(request, exeption):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
