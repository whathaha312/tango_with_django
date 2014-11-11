from django.http import HttpResponse
#from django.template import render
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': "I am the bold font from the context"}
    return render(request, 'rango/index.html', context_dict) 

def about(request):
#    return HttpResponse("Rango says here is the about page. <a href='/rango'>index</a>")
    context_dict = {'boldmessage': "About..."}
    return render(request, 'rango/about.html', context_dict) 
