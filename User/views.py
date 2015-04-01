from django.shortcuts import render, get_object_or_404
from django.core.context_processors import request
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from User.forms import UserLogin

# Create your views here.
def index(request):
#     user = request.user
#     if not user.is_authenticated():
    return HttpResponseRedirect(reverse('user:login'))

def Login(request):
    #     user = request.user
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user = authenticate(
            username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('Things:index'))
            else:
                return HttpResponseRedirect(reverse('user:login'))

    form = UserLogin()
    return render(request, 'User/user_login_form.html', {'form': form})

def Logout(request):
    user = request.user
    logout(request)
#     if not user.is_authenticated():
    return HttpResponseRedirect(reverse('user:login'))
