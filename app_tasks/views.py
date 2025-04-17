from django.shortcuts import render

# Create your views here.
def dashboard(request):
    """
    Dashboard view.
    """
    return render(request, 'app_tasks/dashboard.html')