from django.core.management.base import BaseCommand, CommandError
from openfoodfacts.models import Product, Brand, Categorie, ProductBrand, ProductCategorie, Nutritiongrade
from requests.exceptions import HTTPError


class Command(BaseCommand):
    help = 'Empty all the models of openfoodfacts in the database'


    def handle(self, *args, **options):
        #We are getting all our datas from the database
        product = Product.objects.all()
        brand = Brand.objects.all()
        categorie = Categorie.objects.all()
        productbrand = ProductBrand.objects.all()
        productcategorie = ProductCategorie.objects.all()
        nutritiongrade = Nutritiongrade.objects.all()

        #We delete the datas from the database
        print("Deleting datas from ProductBrand")
        productbrand.delete()
        print("Deleting datas from ProductCategorie")
        productcategorie.delete()
        print("Deleting datas from Nutritiongrade")
        nutritiongrade.delete()
        print("Deleting datas from Brand")
        brand.delete()
        print("Deleting datas from Categorie")
        categorie.delete()
        print("Deleting datas from Product")
        product.delete()