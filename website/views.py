from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index_view(request):
    return HttpResponse("<h1>Home Page</h1>")

def about_view(request):
    return HttpResponse("<h2>About Page</h2>")

def contact_view(request):
    return HttpResponse("<h2>Contact Page</h2>")

def json_test(request):
    return JsonResponse({'name': 'Mr.BoO', 'description': 'Scary funny little ghost'})