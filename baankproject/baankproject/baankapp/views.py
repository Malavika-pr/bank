from django.contrib import auth, messages

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.contrib import messages

from baankapp.forms import CustomerDetailsForm


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('baankapp:newpage')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if not username:
            messages.error(request, 'Username cannot be empty.')
            return redirect('baankapp:register')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('baankapp:register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken')
            return redirect('baankapp:register')

        user = User.objects.create_user(username=username, password=password)

        if user:

            auth.login(request, user)
            # messages.success(request, 'Registration successful')
            return redirect('baankapp:login')
        else:
            messages.error(request, 'Error creating user')

    return render(request, 'register.html')


def newpage(request):
    if request.method == 'POST':
        form = CustomerDetailsForm(request.POST)
        if form.is_valid():
            # customer = form.save(commit=True)
            # customer.materials_provided.set(form.cleaned_data['materials_provided'])
            # customer.save()
            form.save()

            return redirect('baankapp:success_page')
    else:
        form = CustomerDetailsForm()

    return render(request, 'newpage.html', {'form': form})


def success_page(request):
    return render(request, 'success_page.html')


