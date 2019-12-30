from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('connexion', views.connexion, name="connexion"),
    path('create_account', views.create_account, name="create_account"),
    path('deconnexion', views.deconnexion, name="deconnexion"),
    path('profile', views.profile, name="profile"),
    path('aliment', views.aliment, name="aliment")
]