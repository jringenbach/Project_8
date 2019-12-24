from django.contrib.auth.models import User
from django import forms



class UserForm(forms.ModelForm):
    """Form that we use for users to create their account"""

    def __init__(self, *args):
        super().__init__()
        self.fields['username'].widget.attrs.update({"class" : "create_input"})
        self.fields['password'].widget.attrs.update({"class" : "create_input"})
        self.fields["email"].widget.attrs.update({"class" : "create_input"})

        #We remove the help text from the fields
        for field in ["username", "password", "email"]:
            self.fields[field].help_text = None



    class Meta:
        model = User
        exclude = ("groups", "user_permissions", "is_staff", "is_active", "is_superuser", "last_login", "date_joined", "first_name", "last_name")



    def clean_username(self):
        """Method to clean the username. """
        username = self.cleaned_data["username"]

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



    def clean_password(self):
        """Method to set some rules for the password"""

        password = self.cleaned_data["password"]

        #If the password length is inferior to 
        if len(password) < 8:
            raise forms.ValidationError("Le mot de passe doit contenir au moins 8 caractères.")

        return password

    
