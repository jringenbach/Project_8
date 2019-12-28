from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import CreateAccountForm, ConnexionForm



# Create your views here.
def index(request):
    """Index page of the website purbeurre"""

    return render(request, "openfoodfacts/index.html")



def connexion(request):
    """Connexion page where user can log in"""
    form = ConnexionForm(request.POST or None)

    if form.is_valid():
        pass

    return render(request, "openfoodfacts/connexion.html", locals())



def create_account(request):
    """Page where users can create their account"""

    form = CreateAccountForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        email = form.cleaned_data["email"]
        User.objects.create_user(username=username, password=password, email=email)

        envoi = True

    return render(request, "openfoodfacts/create_account.html", locals())
