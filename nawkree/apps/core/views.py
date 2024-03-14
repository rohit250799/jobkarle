from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def frontpage(request):
    return render(request, 'core/frontpage.html')

@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out succesfully")
    return render(request, 'core/login.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('frontpage')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {
        'form': form,
    })