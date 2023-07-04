from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-index')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'user/signup.html', context)

def profile(request):
     return render(request, 'user/profile.html')
