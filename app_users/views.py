from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, SignInForm
from django.contrib.auth.decorators import login_required


# View for the landing page
def landing_page(request):
    """
    Landing page view.
    Renders the base template.
    """
    return render(request, 'base.html')


# View for user signup/registration
def signup_view(request):
    # Check if the request is a POST (i.e., form submission)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Save the user but don't commit to the DB yet
            user = form.save(commit=False)
            # Hash the password before saving
            user.set_password(form.cleaned_data['password'])
            user.save()
            # Show success message
            messages.success(request, "Account created successfully.")
            # Redirect user to the sign-in page
            return redirect('signin')
    else:
        # If GET request, just render an empty form
        form = SignUpForm()

    # Render the signup page with the form
    return render(request, 'app_users/signup.html', {'form': form})


# View for user signin/login
def signin_view(request):
    # Check if the request is a POST (i.e., form submission)
    if request.method == 'POST':
        # Bind form with POST data
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            # Extract cleaned username and password
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Login the user and redirect to dashboard
                login(request, user)
                return redirect('dashboard')  # Redirect to your dashboard or main page
            else:
                # If authentication failed, show error
                messages.error(request, "Invalid credentials.")
    else:
        # If GET request, just render an empty form
        form = SignInForm()

    # Render the signin page with the form
    return render(request, 'app_users/signin.html', {'form': form})


# View for user signout/logout
def signout_view(request):
    # Log the user out
    logout(request)
    # Redirect to signin page after logout
    return redirect('signin')
