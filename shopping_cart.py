# shopping_cart.py

import os
from datetime import datetime
from pandas import read_csv


#allow the user to input their own tax rate by passing an environment variable called TAX_RATE
tax_rate = os.getenv("TAX_RATE", default=0)


csv_filepath = "data/products.csv"
x = read_csv(csv_filepath)

products = x.to_dict("records")

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

#find date and time
now = datetime.now()
date_time = now.strftime("%m/%d/%Y %H:%M")

billTotal = sum(matching_prices)
taxTotal = billTotal*(float(tax_rate)/100)
total = billTotal + taxTotal

print("---------------------------------")
print("GEORGETOWN GROCERIES")
print("WWW.GEORGETOWN-GROCERIES.COM")
print("---------------------------------")
print("CHECKOUT AT:", date_time)
print("---------------------------------")
print("SELECTED PRODUCTS:")

for x in matching_products:
    indexNum = matching_products.index(x)
    print("...", x, "("+ str(to_usd(matching_prices[indexNum])) +")")
print("---------------------------------")
print("SUBTOTAL:", to_usd(billTotal))
print("TAX:", to_usd(taxTotal))
print("TOTAL:", to_usd(total))
print("---------------------------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("---------------------------------")

emailReceipt = "stesd" #set initial value to random string to ensure while loop runs

while emailReceipt.lower() != "yes" and emailReceipt.lower() != "no":
    print()
    print("Would the customer like a receipt to be emailed to them?")
    emailReceipt = input("Please enter Yes or No: ")

if emailReceipt.lower() == "yes":
    import os
    from dotenv import load_dotenv
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail

    load_dotenv()

    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
    SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")
    customer_address = input("Please input the customer's email address: ")

    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    print("CLIENT:", type(client))

    subject = "Your Receipt from Georgetown Groceries"

    ###############CREATE EMAIL RECEIPT#####################

    
    html_list_items = ""

    for x in matching_products:
        indexNum = matching_products.index(x)
        priceString = str(to_usd(matching_prices[indexNum]))
        productAndPriceString = x + " ("+ str(to_usd(matching_prices[indexNum])) +")"
        html_list_items += "<li>"+productAndPriceString+"</li>"


    html_content = f"""
    <h3>Hello this is your receipt</h3>
    <p>You Ordered:</p>
    <ol>
        {html_list_items}
    </ol>
    <p>THANKS, SEE YOU AGAIN SOON!</p>
    """
    print(html_content)


    ######################################

  
    message = Mail(from_email=SENDER_ADDRESS, to_emails=customer_address, subject=subject, html_content=html_content)

    try:
        response = client.send(message)

        print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
        print(response.status_code) #> 202 indicates SUCCESS
        print(response.body)
        print(response.headers)

    except Exception as err:
        print(type(err))
        print(err)
