from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# ******************************** Change password ********************************
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
# ******************************** Change password ********************************

# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            msg=""
            # ********************************************************* Checking that login is done with email or username and handle it *********************************************************
            username = request.POST.get('username')
            password = request.POST.get('password')
            author = User.objects.filter(email=username).first()
            if author is not None:
                request.POST._mutable = True
                request.POST['username'] = author
            form = AuthenticationForm(request=request, data=request.POST)
            # ********************************************************* Checking that login is done with email or username and handle it *********************************************************
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
           
            # ******************************** Print just form.error_messages[invalid_login] element ********************************
            if form.errors:
                for field in form.errors:
                    print(form.errors)
                    for error in form.errors[field]:
                        msg = msg + f"<p>{error}</p>"
            messages.add_message(request, messages.ERROR, msg)
            # ******************************** Print just form.error_messages[invalid_login] element ********************************

            # ******************************** Print just form.error_messages[all elemants] element ********************************
            # if form.errors:
            #     key = True
            #     for field in form.error_messages:
            #         if key == True:
            #             msg = msg + f"<p>{form.error_messages[field]}</p>or<p></p>"
            #             key = False
            #         else:
            #             msg = msg + f"<p>{form.error_messages[field]}</p>"
            # ******************************** Print just form.error_messages[all elemants] element ********************************

            messages.add_message(request, messages.ERROR, msg)
            
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
            msg=""
            form = UserCreationForm(request.POST)
            if form.is_valid():
                # Update values before save ****************************************************************
                obj = form.save(commit=False)
                obj.email = request.POST.get('email')
                # Update values before save ****************************************************************
                messages.add_message(request, messages.SUCCESS, 'Your register is done successfully')
                form.save()
                return redirect('/accounts/login/')
            if form.errors:
                for field in form:
                    for error in field.errors:
                        msg = msg + f'<p>{error}</p>'
            messages.add_message(request, messages.ERROR, msg)
        return render(request, 'accounts/signup.html')
    else:
        return redirect('/')

# **************************************** Some rolls for change password ****************************************
# Your password can’t be too similar to your other personal information.
# Your password must contain at least 8 characters.
# Your password can’t be a commonly used password.
# Your password can’t be entirely numeric.
# **************************************** Some rolls for change password ****************************************
@login_required   
def change_password_view(request):
    if request.method == 'POST':
        msg = ""
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            if form.errors:
                for field in form.errors:
                    for error in form.errors[field]:
                        msg = msg + f"<p>{error}</p>"
            messages.error(request, msg)
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })

