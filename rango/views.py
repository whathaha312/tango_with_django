from django.http import HttpResponse
#from django.template import render
from django.shortcuts import render
from rango.models import Category
from rango.forms import CategoryForm

def index(request):
    #context_dict = {'boldmessage': "I am the bold font from the context"}
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context_dict) 

def about(request):
#    return HttpResponse("Rango says here is the about page. <a href='/rango'>index</a>")
    context_dict = {'boldmessage': "About..."}
    return render(request, 'rango/about.html', context_dict) 

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = CategoryForm()

    return render(request, 'rango/add_category.html', {'form': form})
