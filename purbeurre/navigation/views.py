from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import CreateAccountForm, ConnexionForm



# Create your views here.
def index(request):
    """Index page of the website purbeurre"""

    return render(request, "navigation/index.html")



def connexion(request):
    """Connexion page where user can log in"""
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return(redirect(index))
            else:
                error = True
    
    else:
        form = ConnexionForm()

    return render(request, "navigation/connexion.html", locals())




def deconnexion(request):
    """Action when user wants to log out of the website"""
    logout(request)
    return redirect(index)



def create_account(request):
    """Page where users can create their account"""

    form = CreateAccountForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        email = form.cleaned_data["email"]
        User.objects.create_user(username=username, password=password, email=email)

        envoi = True

    return render(request, "navigation/create_account.html", locals())



def profile(request):
    """Profile page of the user"""

    return render(request, "navigation/profile.html", locals())