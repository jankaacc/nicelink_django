
from django.shortcuts import render, get_object_or_404
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from ..forms import UserRegisterForm, UserLoginForm




def register_view(request):
    title = 'Register'
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserRegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # link = Link.objects.create_link(form.cleaned_data['oryginal_link'])
            print('form valid')
            try:
                user = form.save(commit=False)
                password = form.cleaned_data.get('password')
                user.set_password(password)
                user.save()
                flag = False
            except IntegrityError:
                print(IntegrityError)
            return HttpResponseRedirect(reverse('nicelink:index'))
    else:
        form = UserRegisterForm()
    return render(request, 'nicelink/user.html', {'form': form})


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request,user)
        if next:
            return redirect(next)
    return render(request, 'nicelink/login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('nicelink:index')




