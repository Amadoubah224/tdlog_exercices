"""
We want to have a new class Item such as :

A new item can be created with Item(price, weight)
    The price and weight of an item can be accessed with
    item.price and item.weight.
    Write the code for this class, with the appropriate constructor.
Example of code using the class: i = Item(10, 20)
"""
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Item:
    def __init__(self, price, weight):
        # Logging the creation of a new item with its price and weight
        logging.info(f"Creating an Item with price: {price} and weight: {weight}")
        self.price = price
        self.weight = weight

    @property
    def price(self):
        logging.info(f"Accessing the price: {self._price}")
        return self._price

    @price.setter
    def price(self, value):
        logging.info(f"Setting price to: {value}")
        self._price = value

    @property
    def weight(self):
        logging.info(f"Accessing the weight: {self._weight}")
        return self._weight

    @weight.setter
    def weight(self, value):
        logging.info(f"Setting weight to: {value}")
        self._weight = value

# Example of using the class
i = Item(10, 20)
logging.info(f"Item price: {i.price}")
logging.info(f"Item weight: {i.weight}")
