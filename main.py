# Program that utilizes upcitemdb's RESTful API to get information based on an item's UPC.
# Note: color field usually only populates for clothing/shoes.
from getRequest import get_item_details

def main():

    # User inputs the product's upc to get information about it 
    user_input_upc = input("Please enter UPC for item: ")
    print("\n\n")

    #Call function to assign variables appropriately
    upc, product, brand_name, model, color, lowest_price, product_link = get_item_details(user_input_upc)

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