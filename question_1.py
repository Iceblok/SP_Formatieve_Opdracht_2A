import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")

# Connect to the wanted database in MongoDB
db = client["TestHuWebshop"]

# Collections out of the database
products = db["products"]
profiles = db["profiles"]
sessions = db["sessions"]

all_products = products.find({})

"""Question 1"""
print("Wat is de naam en prijs van het eerste product in de database?")


def get_first_product():
    """Function returns first product of the database"""
    first_product = all_products[0]
    first_product_name = first_product["name"]
    first_product_price = first_product["price"]["selling_price"]
    return f"Naam: {first_product_name}\nPrijs: {first_product_price}"


print(get_first_product())