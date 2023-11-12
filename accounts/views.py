from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.add_message(request, messages.SUCCESS, 'You have been logged in successfully')
                    # ************************************* Redirect to before post after login else go to home page *************************************
                    if 'next' in request.POST:
                        return redirect(request.POST.get('next'))
                    else:
                        return redirect('/')
                    # ************************************* Redirect to before post after login else go to home page *************************************
            messages.add_message(request, messages.ERROR, 'Your informations is NOT valid')
        return render(request, 'accounts/login.html')
    else:
        return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def register_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                # Update values before save ****************************************************************
                obj = form.save(commit=False)
                obj.email = request.POST.get('email')
                # Update values before save ****************************************************************
                messages.add_message(request, messages.SUCCESS, 'Your register is done successfully')
                form.save()
                return redirect('/accounts/login/')
            messages.add_message(request, messages.ERROR, 'Your register is failed')
        return render(request, 'accounts/signup.html')
    else:
        return redirect('/')