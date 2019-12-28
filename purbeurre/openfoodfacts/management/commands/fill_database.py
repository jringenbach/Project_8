from django.core.management.base import BaseCommand, CommandError
from openfoodfacts.models import Product, Brand, Categorie, ProductBrand, ProductCategorie, Nutritiongrade
import requests
from requests.exceptions import HTTPError


class Command(BaseCommand):
    help = 'Insert datas from openfoodfacts API to the postgresql database'


    def handle(self, *args, **options):
        list_categorie = ["biscuits", "cereales-et-pommes-de-terre", "confiseries", "fromages-de-france", "pains", "poissons", "viande", "boissons", "pizza", "snacks-sucres"]
        url = "https://fr.openfoodfacts.org/cgi/search.pl"

        #Parameters of the GET request to openfoodfacts API
        params = {
            "action" : "process",
            "json" : 1,
            "tagtype_0" : "categories",
            "tag_contains_0" : "contains",
            "tag_0" : "",
            "page_size" : "50"
        }

        try:
            #We look for products for each categorie defined above
            for name_categorie in list_categorie:
                print("Inserting "+name_categorie+" products into database")
                params["tag_0"] = name_categorie
                products_json = requests.get(url, params=params)
                products_json = products_json.json()

                #If the Categorie doesn't already exist
                categorie, categorie_created = Categorie.objects.get_or_create(name_categorie=name_categorie)
                if categorie_created:
                    categorie.save()
                
                #We get datas for each product
                for product_json in products_json["products"]:
                    if "product_name" in product_json.keys() and "nutrition_grades" in product_json.keys() \
                    and "brands" in product_json.keys() and "code" in product_json.keys() and "image_small_url" in product_json.keys() \
                    and "image_url" in product_json.keys() and "url" in product_json.keys():
                        name_brand = product_json["brands"]
                        nutritiongrade = product_json["nutrition_grades"]
                        barcode = product_json["code"]
                        image_small_url = product_json["image_small_url"]
                        image_url = product_json["image_url"]
                        url = product_json["url"]
                        product_name = product_json["product_name"]

                        #If the brand doesn't already exist
                        brand, brand_created = Brand.objects.get_or_create(name_brand=name_brand)
                        if brand_created:
                            brand.save()

                        #If the Nutritiongrade doesn't already exist
                        nutrition_grade, nutrition_grade_created = Nutritiongrade.objects.get_or_create(nutrition_grade=nutritiongrade)
                        if nutrition_grade_created:
                            nutrition_grade.save()


                        product, product_created = Product.objects.get_or_create(barcode=barcode, url=url, product_name=product_name, image_url = image_url, image_small_url=image_small_url, nutrition_grade=nutrition_grade)
                        if product_created:
                            product.save()
                        productbrand = ProductBrand.objects.create(product=product, brand=brand)
                        productbrand.save()
                        productcategorie = ProductCategorie.objects.create(product=product, categorie=categorie)
                        productcategorie.save()

                        
        except HTTPError as e:
            print(e)