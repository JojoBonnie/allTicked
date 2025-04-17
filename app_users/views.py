from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, SignInForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def landing_page(request):
    """
    Landing page view.
    """
    return render(request, 'base.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Account created successfully.")
            return redirect('signin')
    else:
        form = SignUpForm()
    return render(request, 'app_users/signup.html', {'form': form})

def signin_view(request):
    if request.method == 'POST':
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # or wherever your homepage is
            else:
                messages.error(request, "Invalid credentials.")
    else:
        form = SignInForm()
    return render(request, 'app_users/signin.html', {'form': form})

def signout_view(request):
    logout(request)
    return redirect('signin')

