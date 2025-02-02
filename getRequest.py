# Function that makes a HTTP GET request to upcitemdb's RESTful API then parses the data to return desired values. 
import requests
import json

def get_item_details(upc_code): # upc_code will be defined by the user
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip,deflate',
    'user_key': 'only_for_dev_or_pro', # Used for trial version
    'key_type': '3scale'
    }
    resp = requests.get('https://api.upcitemdb.com/prod//trial/lookup?upc=' + upc_code, headers=headers) #inputting user's desired UPC into the request
    data = json.loads(resp.text) # Formatting the request into a data object
    item_details = [item for item in data['items']] # Use list comprehension to create a list of the item's details

    # Loop through the list, item_details, to assign appropriate values to each variable
    for detail in item_details:
        upc = detail['upc']
        product = detail['title']
        brand_name = detail['brand']
        model = detail['model']
        color = detail['color']
        lowest_price = detail['lowest_recorded_price']
        for offer in detail['offers']:
            product_link = offer['link']

    return upc, product, brand_name, model, color, lowest_price, product_link