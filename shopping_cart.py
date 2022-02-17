# shopping_cart.py

import os
from datetime import datetime

#allow the user to input their own tax rate by passing an environment variable called TAX_RATE
tax_rate = os.getenv("TAX_RATE", default=0)


products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

# TODO
#fix while loop for non-number invalid input

print("This system will help you check items out!")
print("To use it, enter product identifiers for each item or enter DONE when finished.")
print()

matching_products = []
matching_prices = []
product_ID = "wrongInput"

while True:
    product_ID = input("Please input a product identifier: ")

    if product_ID.lower() == "done": #allows user to exit while loop when out of products
        break

    #LOOK UP CORRESPONDING PRODUCTS & PRICES
    
    try: #makes sure user only enters numeric data / loop goes on despite non-numeric data
        for x in products:
            if x["id"] == int(product_ID):  #this is a match
                matching_products.append(x["name"])
                matching_prices.append(x["price"])
    except:
        print("Invalid. Please only enter numeric data or DONE when finished.")

now = datetime.now()
date_time = now.strftime("%m/%d/%Y %H:%M")

billTotal = sum(matching_prices)
taxTotal = billTotal*(tax_rate/100)
total = billTotal + taxTotal

print("---------------------------------")
print("GEORGETOWN GROCERIES")
print("WWW.GEORGETOWN-GROCERIES.COM")
print("---------------------------------")
print("CHECKOUT AT:", date_time)
print("---------------------------------")
print("SELECTED PRODUCTS:")

for x in in matching_products:
    indexNum = matching_products.index(x)
    print("...", x, "("+ matching_products(indexNum) +")")
print("---------------------------------")
print("SUBTOTAL:", billTotal)
print("TAX:", taxTotal)
print("TOTAL:", total)
print("---------------------------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("---------------------------------")