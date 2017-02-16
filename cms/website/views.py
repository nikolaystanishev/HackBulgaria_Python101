from django.shortcuts import render, redirect

from website.models import User
from website.decorators import login_required, annon_required
from website.forms import LoginForm
from website.forms2 import RegisterForm


# Create your views here.
@annon_required(redirect_url='/profile')
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['email'] = request.POST['email']
            return redirect('/profile')
    form = RegisterForm()
    return render(request, 'register.html', locals())


@annon_required(redirect_url='/profile')
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.find()
            if u:
                request.session['email'] = request.POST['email']
                return redirect('/profile')
    form = LoginForm()
    return render(request, 'login.html', locals())


@login_required(redirect_url='/login')
def profile(request):
    if request.method == 'GET':
        u = User.objects.filter(email=request.session['email']).first()
    return render(request, 'profile.html', locals())
