from django.http import HttpResponse, HttpResponseRedirect
#from django.template import render
from django.shortcuts import render
from rango.models import Category
from rango.forms import CategoryForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
        
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
    
            profile.save()
            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 
        'rango/register.html',
        {'user_form': user_form, 'profile_form': profile_form, 
        'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/rango/')
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password) 
            return HttpResponse("Invalid login details supplied.")
    else: 
        return render(request, 'rango/login.html', {}) 

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/rango/')
