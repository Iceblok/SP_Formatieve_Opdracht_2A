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
    return f"Naam: {first_product_name}\nPrijs: {first_product_price}\n"


print(get_first_product())


"""Question 2"""
print("Geef de naam van het eerste product waarvan de naam begint met een 'R'?")


def search_with_first_letter(letter: str):
    """
    Function returns the name of the first product based of the given letter.
    @param letter: str, example 'R'
    @return: str, output RCF V-MAX V35 passieve 15 inch luidspreker 3600W
    """
    letter = letter.upper()
    for product in all_products:
        product_name = product["name"]
        first_letter_of_product = product_name[0].upper()
        if first_letter_of_product == letter:
            return product_name


print(f"Naam: {search_with_first_letter('R')}\n")


"""Question 3"""
print("Wat is de gemiddelde prijs van de producten in de database?")


def average_price():
    """Function returns the average price of the products out of the database"""
    price_list = []
    for product in all_products:
        price_list.append(product["price"]["selling_price"])
    return sum(price_list) / len(price_list)


print(average_price())
