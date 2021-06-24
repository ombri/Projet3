from .forms import LogForm, SignForm

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from django.contrib.auth import login as auth_login, logout as auth_logout
from app2.models import Forum


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'app1/index.html')
    else:
        username = request.user.username
        return render(request, 'app1/index-connected.html', {"username": username})


def logout(request):
    auth_logout(request)
    return redirect('http://127.0.0.1:8000')


def base(request):
    return render(request, 'app1/base.html')


def signin(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data["F_username"]
            Fname = form.cleaned_data["F_Fname"]
            Lname = form.cleaned_data["F_Lname"]
            email = form.cleaned_data["F_email"]
            pwd = form.cleaned_data["F_password"]
            confi = form.cleaned_data["conf_password"]
            member_group = Group.objects.get(name='member')
            if confi != pwd:
                return HttpResponseRedirect('')
            else:
                if len(User.objects.filter(username=user)) != 0:
                    return HttpResponseRedirect('app1/signin.html')
                else:
                    u = User.objects.create_user(user, email, pwd, first_name=Fname, last_name=Lname)
                    u.save()
                    user_g = User.objects.get(username=user)
                    member_group.user_set.add(user_g)
                return redirect('http://127.0.0.1:8000')
    else:
        form = SignForm()
    return render(request, 'app1/signin.html', {"form": form})


def login(request):
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["check_username"]
            password = form.cleaned_data["check_password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('http://127.0.0.1:8000')
            else:
                return render(request, 'app1/login.html', {"form": form})
        else:
            form = LogForm()
        return render(request, 'app1/login.html', {"form": form})
    return render(request, 'app1/login.html')



def profile(request):
    username = request.user.username
    email = request.user.email
    password = request.user.password
    Fname = request.user.first_name
    Lname = request.user.last_name
    forum = Forum.objects.filter(author=username)
    return render(request, 'app1/profile.html', {"username": username,
                                                 "email": email,
                                                 "password": password,
                                                 "Fname": Fname,
                                                 "Lname": Lname,
                                                 "forum": forum})

def userDelete(request):
    username = request.user.username
    u = User.objects.get(username = username)
    u.delete()
    return render(request, 'app1/index.html')

def delete(request,article):
    Forum.objects.filter(author=request.user.username).filter(topic=article).delete()
    return redirect('http://127.0.0.1:8000/profile/')

def userChangeInformations(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.cleaned_data["F_username"]
            Fname = form.cleaned_data["F_Fname"]
            Lname = form.cleaned_data["F_Lname"]
            email = form.cleaned_data["F_email"]
            pwd = form.cleaned_data["F_password"]
            confi = form.cleaned_data["conf_password"]
            print(user, Fname, Lname, email, pwd)
            if confi != pwd:
                return HttpResponseRedirect('')
            else:
                User.objects.filter(username=request.user.username).update(first_name = Fname)
                User.objects.filter(username=request.user.username).update(last_name = Lname)
                User.objects.filter(username=request.user.username).update(email = email)
                User.objects.filter(username=request.user.username).update(password = pwd)
                User.objects.filter(username=request.user.username).update(username = user)
            return redirect('http://127.0.0.1:8000/profile/')
    else:
        form = SignForm()
    return render(request, 'app1/UserChangeInfo.html', {"form": form})


