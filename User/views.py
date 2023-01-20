from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You are now able to login!')
            return redirect('user-login')

    else:
        form = UserRegisterForm()
    context = {
        'form':form
    }
    return render(request, "User/register.html", context)
@login_required
def profile(request):
    return render(request, 'User/profile.html')