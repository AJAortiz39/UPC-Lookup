# Program that utilizes upcitemdb's RESTful API to get information based on an item's UPC.
# Note: color field usually only populates for clothing/shoes.
import requests
import json

def main():

    # User inputs the product's upc to get information about it 
    user_upc = input("Please enter UPC for item: ")
    print("\n\n")

    # Necessary headers to make a HTTP GET request
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip,deflate',
    'user_key': 'only_for_dev_or_pro', # Used for trial version
    'key_type': '3scale'
    }
    resp = requests.get('https://api.upcitemdb.com/prod//trial/lookup?upc=' + user_upc, headers=headers) #inputting user's desired UPC into the request
    data = json.loads(resp.text) # Formatting the request into a data object then assigning values to each variable
    item_details = [item for item in data['items']] # Use list comprehension to create a list of the item's details
    # Loop through the list item_details to assign appropriate values to each field
    for detail in item_details:
        upc = detail['upc']
        product = detail['title']
        brand_name = detail['brand']
        model = detail['model']
        color = detail['color']
        lowest_price = detail['lowest_recorded_price']
        for offer in detail['offers']:
            product_link = offer['link']
    
    #Print out information
    print("Product: " + product +
          "\nBrand: " + brand_name +
          "\nModel: " + model +
          "\nColor: " + color +
          "\nLowest Price: " +  str(lowest_price) +
          "\nProduct Link: " + product_link +
          "\nUPC: " + upc)


if __name__ == "__main__":
    main()