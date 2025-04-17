from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


# Form for user registration/signup
class SignUpForm(forms.ModelForm):
    # Add a password field with a password input widget to hide characters
    password = forms.CharField(widget=forms.PasswordInput)
    # Add a confirm password field to ensure password confirmation
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        # Link the form to Django's built-in User model
        model = User
        # Specify the fields from the User model to include in the form
        fields = ['username', 'email', 'password']

    # Custom validation method for the form
    def clean(self):
        # Get the cleaned form data
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        # Check if both passwords are provided and match
        if password and confirm_password and password != confirm_password:
            # Raise a validation error if passwords do not match
            raise forms.ValidationError("Passwords do not match.")

        # Return the cleaned data after validation
        return cleaned_data


# Form for user login/signin
class SignInForm(AuthenticationForm):
    # Override the default fields to use standard form fields
    username = forms.CharField()  # Input field for username
    password = forms.CharField(widget=forms.PasswordInput)  # Password input with hidden characters
