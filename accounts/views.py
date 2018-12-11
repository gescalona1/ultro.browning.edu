from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import modelformset_factory
from django.contrib.auth import get_user_model
from django.contrib.auth import (
    authenticate, login as auth_login, logout as auth_logout
)
from .forms import MemberCreationForm, MemberLogForm
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.


def signup(request):

    if request.method == 'POST':
        form = MemberCreationForm(request.POST)
        if form.is_valid():
            member = form.save()
            print(member.password)
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
                return redirect('notebook')
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
    return redirect("index")


@login_required
@permission_required("accounts.can_view_notebook", raise_exception=True)
def notebook(request):
    user = request.user
    return HttpResponse(f"Hello {user.username}")

