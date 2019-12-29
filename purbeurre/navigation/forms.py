from django.contrib.auth.models import User
from django import forms
import re



class ConnexionForm(forms.Form):
    """Form that we use to help user to connect to the website"""

    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args):
        super().__init__(*args)

        #We add the class create_input to our fields
        self.fields['username'].widget.attrs.update({"class" : "create_input"})
        self.fields['password'].widget.attrs.update({"class" : "create_input"})

        #We change the label of the fields
        self.fields["username"].label = "Nom d'utilisateur"
        self.fields["password"].label = "Mot de passe"



class CreateAccountForm(forms.ModelForm):
    """Form that we use for users to create their account"""

    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args):
        super().__init__(*args)

        #We add the class create_input to our fields
        self.fields['username'].widget.attrs.update({"class" : "create_input"})
        self.fields['password'].widget.attrs.update({"class" : "create_input"})
        self.fields["email"].widget.attrs.update({"class" : "create_input"})

        #We change the label of the fields
        self.fields["username"].label = "Nom d'utilisateur"
        self.fields["password"].label = "Mot de passe"
        self.fields["email"].label = "Adresse e-mail"

        #We remove the help text from the fields
        for field in ["username", "password", "email"]:
            self.fields[field].help_text = None



    class Meta:
        model = User
        fields = ["username", "email","password"]
        exclude = ("groups", "user_permissions", "is_staff", "is_active", "is_superuser", "last_login", "date_joined", "first_name", "last_name")



    def clean_username(self):
        """Method to clean the username. """
        username = self.cleaned_data["username"]

        #If the username has characters different than numbers, letters or - and _
        if not re.match("^[A-Za-z0-9_-]*$", username):
            raise forms.ValidationError("Le nom d'utilisateur ne doit contenir que des lettres")

        #If the username already exists
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Ce nom d'utilisateur existe déjà")

        return username

    

    def clean_email(self):
        """Method to clean the email field"""

        email = self.cleaned_data["email"]

        #If the email already exists
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Cette adresse e-mail est déjà utilisée!")

        return email

    
