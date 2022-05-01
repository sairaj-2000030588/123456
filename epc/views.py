from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee


# Create your views here.
def home(request):
    return render(request, 'epc/home.html', {'title': 'HOME'})


def about(request):
    return render(request, 'epc/about.html', {'title': 'ABOUT'})


def signup(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewS')
    else:
        form = EmployeeForm()
    return render(request, 'epc/signup.html', {'title': 'Register', 'form': form})


def view_employee(request):
    return render(request, 'epc/view_employee.html', {'title': 'View Employees', 'employee': Employee.objects.all()})

def contact(request):
    return render(request, 'epc/contact.html', {'title': 'CONTACT US'})

def login(request):
    return render(request, 'epc/login.html', {'title': 'LOGIN'})

def applyform(request):
    return render(request, 'epc/applyform.html', {'title': 'APPLY'})
