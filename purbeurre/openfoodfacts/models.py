from django.db import models
from django.contrib.auth.models import User



# Create your models here.
#Stores non obligatoires : à enlever
class Store(models.Model):
    """Class that represents the store in the database
    id_store : unique identifier of a store (int)
    name_store : name of a store (string)"""
    id_store = models.IntegerField(primary_key=True)
    name_store = models.CharField(max_length=30)



class Categorie(models.Model):
    """Class that represents the store in the database
    id_categorie : unique identifier of a categorie (int)
    name_categorie : name of a categorie (string)"""

    id_categorie = models.IntegerField(primary_key=True)
    name_categorie = models.CharField(max_length=50)



class Brand(models.Model):
    """Class that represents the store in the database
    id_brand : unique identifier of a brand (int)
    name_brand : name of a brand (string)"""

    id_brand = models.IntegerField(primary_key=True)
    name_brand = models.CharField(max_length=80)



class Nutritiongrade(models.Model):
    """Class that represents the nutrition grade of a product
    nutrition_grade : nutriscore represented by a character from A to F (string)"""

    nutrition_grade = models.CharField(max_length=1, primary_key=True)


#ajouter l'url de l'image
#ajouter l'url de l'image de l'étiquette nutritionnelle
class Product(models.Model):
    """A product that we got from openfoodfacts API
    barcode : barcode of the product (string)
    product_name : name of the product (string)
    url : url where to find the details about the product (string)
    nutrition_grade : Nutriscore of the product (Nutritiongrade)"""

    barcode = models.CharField(max_length=20, primary_key=True)
    product_name = models.CharField(max_length=100)
    url = models.CharField(max_length=150)
    nutrition_grade = models.ForeignKey(Nutritiongrade, on_delete=models.CASCADE)



class ProductBrand(models.Model):
    """Intermediate table that represents the many-to-many relationship between a product and a brand
    barcode : barcode of a product (string)
    id_brand : unique identifier of a brand (int)"""

    barcode = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)



class ProductCategorie(models.Model):
    """Intermediate table that represents the many-to-many relationship between a product and a categorie
    barcode : barcode of a product (string)
    id_categorie : unique identifier of a categorie (int)"""

    barcode = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)



class ProductStore(models.Model):
    """Intermediate table that represents the many-to-many relationship between a product and a store
    barcode : barcode of a product (string)
    id_store : unique identifier of a store (int)"""

    barcode = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_store = models.ForeignKey(Store, on_delete=models.CASCADE)



class UserProduct(models.Model):
    """Intermediate table that represents the many-to-many relationship between an user a product
    email : email of a User (string)
    barcode : barcode of a product (string)"""

    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_products")
    email = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_products")
    barcode = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="user_products")