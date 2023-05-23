import requests
import json
import os
from emailapi import Email
from webhook import Hook

class Bestbuy:

    def __init__(self):
        """
        Constructer that establishes the bestbuy api url,  sets the initial value of having a connection to true, and creates two empty strings for the api request and resulting json file.
        """
        self.api_url = "https://api.bestbuy.com/v1/products(sku%20in%20(6360418))?format=json&apiKey=evtrx3mbnq2ewwx5swdt62du"

        self.request = ""

        self.bestbuy_json = ""

        self.connection = True

    def get(self):
        """
        Requests bestbuys api and converts the response to a json file. Afterwards, data from this json file is selected, specifically looking for the name, price, and link to the product. Also handles the exception in which the connection fails.
        """
        try:
            self.request = requests.get(self.api_url)

            self.bestbuy_json = self.request.json()

            self.availability = self.bestbuy_json["products"][0]["onlineAvailability"]

            self.name = self.bestbuy_json["products"][0]["name"]
    
            self.atclink = self.bestbuy_json["products"][0]["addToCartUrl"]

            self.price = self.bestbuy_json["products"][0]["regularPrice"]

        except ConnectionError:
            self.connection = False
            print("Connection Error")

    def checkStock(self):
        """
        Converts the availability string to a boolean value
        return (boolean) True/False is the item is in stock
        """
        if self.availability == "True":
            return True
        else:
            return False

    def notify(self): 
        """
        Main notification method. Gets the data from bestbuy's api, checks if its in stock, and if so (and there is internet connection) notifies the user through email and discord
        """
        self.get()
        self.checkStock()
        if self.availability and self.connection == True :
            self.webhook = Hook()
            self.webhook.sendAlert(self.atclink, self.name, self.price)
            self.email = Email()
            self.email.send_simple_message(self.atclink, self.name)
        else: 
            print("Out of stock")
