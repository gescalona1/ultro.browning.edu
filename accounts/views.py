from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import modelformset_factory
from .models import Member
from django.contrib.auth import (
  authenticate, login as auth_login, logout as auth_logout
)
from .forms import MemberCreationForm, MemberLogForm
# Create your views here.


def signup(request):

  if request.method == 'POST':
    form = MemberCreationForm(request.POST)
    if form.is_valid():
      member = form.save()
      member.set_password(member.password)
      member.save()
      return redirect("login")
      # do something.
  else:
    form = MemberCreationForm()
  return render(request, 'userform.html', {'form': form})


def login(request):
  if request.user.is_authenticated:
    return HttpResponse("You are already logged in!")
  if request.method == 'POST':
    email = request.POST['email']
    password = request.POST['password']
    print(email, password)
    member = authenticate(email=email, password=password)
    print(member)
    if member is not None:
      if member.is_active:
        auth_login(request, member)
        return HttpResponse(f"SUCCESS LOGGED IN {member.pk} {member.username}")
      else:
        return HttpResponse(f"Failed active test")
    else:
      return HttpResponse(f"failed none test")
  else:
    form = MemberLogForm()
  return render(request, 'logform.html', {'form': form})


def logout(request):
  user = request.user
  auth_logout(request)
  return HttpResponse(f"User {user.username} has logged out")


def notebook(request):
  user = request.user
  if user.is_authenticated:
    return HttpResponse(f"Hello {user.username}")
  else:
    return HttpResponse(f"Unauthorized access")
