from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from openfoodfacts.models import Product, Brand, Nutritiongrade
from .forms import CreateAccountForm, ConnexionForm, ProductForm



def aliment(request):
    """Page where user can see the result of its search for an aliment or see the previous searches"""

    if request.method == "POST":
        productform = ProductForm(request.POST)
        if productform.is_valid():
            #We get the product asked by user in the database
            product_name = productform.cleaned_data["product_name"]
            product = Product.objects.filter(product_name__contains=product_name).order_by('nutrition_grade')

            #We get the first categorie in which belong this product
            product_categorie = product.categories.all()[0]
            categorie_search = Categorie.objects.filter(name_categorie=product_categorie)

            #We look for every product with the same categorie
            productcategorie_from_this_categorie = categorie_search.product_categorie.all()

    return render(request, "navigation/aliment.html", locals())



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