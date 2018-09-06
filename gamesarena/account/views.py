from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# The basic user login form
# We pass the data of the form to a request.POST object containing the username and the password. 
# We clean the data for security and if the user is valid we authenticate him passing the username and password params
# If the user is disabled we inform him to  contact an administrator
# If the user visits initially the page we present an empty login form
# Finally we render the template at account/login.html [GO FIX THE URLS!!!] with form as the template parameter

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'], password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Authenticated successfully...')
                else:
                    return HttpResponse('Account disabled, please contact an administrator.')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form':form})


