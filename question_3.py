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


"""Question 3"""
print("Wat is de gemiddelde prijs van de producten in de database?")


def average_price():
    """Function returns the average price of the products out of the database"""
    price_list = []
    for product in all_products:
        price_list.append(product["price"]["selling_price"])
    return sum(price_list) / len(price_list)


print(f"Gemiddelde prijs: {average_price()}")
