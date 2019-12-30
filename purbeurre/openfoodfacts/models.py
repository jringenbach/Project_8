from django.db import models
from django.contrib.auth.models import User



class Nutritiongrade(models.Model):
    """Class that represents the nutrition grade of a product
    nutrition_grade : nutriscore represented by a character from A to F (string)"""

    nutrition_grade = models.CharField(max_length=1, primary_key=True)




class Categorie(models.Model):
    """Class that represents the store in the database
    id_categorie : unique identifier of a categorie (int)
    name_categorie : name of a categorie (string)"""

    name_categorie = models.CharField(max_length=50)



class Brand(models.Model):
    """Class that represents the store in the database
    id_brand : unique identifier of a brand (int)
    name_brand : name of a brand (string)"""

    name_brand = models.CharField(max_length=80)



class Product(models.Model):
    """A product that we got from openfoodfacts API
    barcode : barcode of the product (string)
    product_name : name of the product (string)
    url : url where to find the details about the product (string)
    nutrition_grade : Nutriscore of the product (Nutritiongrade)"""

    barcode = models.CharField(max_length=20, primary_key=True)
    product_name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    image_small_url = models.CharField(max_length=200)
    nutrition_grade = models.ForeignKey(Nutritiongrade, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Categorie, through="ProductCategorie")
    brands = models.ManyToManyField(Brand, through="ProductBrand")



class ProductBrand(models.Model):
    """Intermediate table that represents the many-to-many relationship between a product and a brand
    barcode : barcode of a product (string)
    id_brand : unique identifier of a brand (int)"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_brand")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="product_brand")



class ProductCategorie(models.Model):
    """Intermediate table that represents the many-to-many relationship between a product and a categorie
    barcode : barcode of a product (string)
    id_categorie : unique identifier of a categorie (int)"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_categorie")
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="product_categorie")



class UserProduct(models.Model):
    """Intermediate table that represents the many-to-many relationship between an user a product
    email : email of a User (string)
    barcode : barcode of a product (string)"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_products")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="user_products")