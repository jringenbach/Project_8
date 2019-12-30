from django.core.management.base import BaseCommand, CommandError
from openfoodfacts.models import Product, Brand, Categorie, ProductBrand, ProductCategorie, Nutritiongrade
import requests
from requests.exceptions import HTTPError


class Command(BaseCommand):
    help = 'Insert datas from openfoodfacts API to the postgresql database'


    def handle(self, *args, **options):
        list_categorie = ["poissons","fromages-de-france","biscuits", "cereales-et-pommes-de-terre", "confiseries" , "pains", "viande", "boissons", "pizza", "snacks-sucres"]
        url_openfoodfacts = "https://fr.openfoodfacts.org/cgi/search.pl"

        #Parameters of the GET request to openfoodfacts API
        params = {
            "action" : "process",
            "json" : 1,
            "tagtype_0" : "categories",
            "tag_contains_0" : "contains",
            "tag_0" : "",
            "page_size" : "200"
        }

        try:
            #We look for products for each categorie defined above
            for name_categorie in list_categorie:
                print("Inserting "+name_categorie+" products into database")
                params["tag_0"] = name_categorie
                products_json = requests.get(url_openfoodfacts, params=params).json()

                #If the Categorie doesn't already exist
                categorie, categorie_created = Categorie.objects.get_or_create(name_categorie=name_categorie)
                
                #We get datas for each product
                for i, product_json in enumerate(products_json["products"]):
                    print(str(i)+". "+product_json["product_name"])
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

                        name_brand = name_brand.split(",")
                        list_brand = list()
                        for br in name_brand:
                            #If the brand doesn't already exist
                            brand, brand_created = Brand.objects.get_or_create(name_brand=br)
                            list_brand.append(brand)

                        #If the Nutritiongrade doesn't already exist
                        nutrition_grade, nutrition_grade_created = Nutritiongrade.objects.get_or_create(nutrition_grade=nutritiongrade)

                        #If the product doesn't already exist
                        product, product_created = Product.objects.get_or_create(barcode=barcode, url=url, product_name=product_name, image_url = image_url, \
                            image_small_url=image_small_url, nutrition_grade=nutrition_grade)

                        for br in list_brand:
                            product.brands.add(br)
                        product.categories.add(categorie)


                        
        except HTTPError as e:
            print(e)
