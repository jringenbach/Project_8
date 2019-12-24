from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm



# Create your views here.
def index(request):
    """Index page of the website purbeurre"""

    return render(request, "openfoodfacts/index.html")



def connexion(request):
    """Connexion page where user can log in"""

    return render(request, "openfoodfacts/connexion.html")



def create_account(request):
    """Page where users can create their account"""

    form = UserForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        email = form.cleaned_data["email"]
        form.save()

        envoi = True

    return render(request, "openfoodfacts/create_account.html", locals())
