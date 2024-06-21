'''
Filename: s.py
Author: Ethan Lemieux
Purpose: Demonstrate the Single Responsibility Principle (SRP)

class Order:
    def __init__(self):
        self.items = []
    
    def store():
        pass
    def calculate_total():
        pass
    def validate_order():
        pass
    def send_order():
        pass
    def update():
        pass
'''

# class that adds or removes items from the order
class Order:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_items(self):
        return self.items

# class that calculates the cost of the order
class PriceCalculator:
    def __init__(self, tax_rate):
        self.tax_rate = tax_rate

    def calculate_total(self, order):
        subtotal = sum(item.price for item in order.items)
        tax = subtotal * self.tax_rate
        return subtotal + tax
    
# class that validates order
class Validate:

    def __init__(self, customer_address):
        self.customer_address = customer_address

    def Check_Item_Availablity(self, stock):
        for item in self.items:
            if isempty(item, stock): # isempty is not implemented
                return("Out of stock")
            else:
                return("In stock")
            
    def Check_Customer_Address(self):
        if isvalid(self.customer_address): # isvalid is not implemented
            return(self.customer_address + " is a valid address")
        else:
            return(self.customer_address + " is not a valid address")
        
# class that sends order confirmation after order processing

class OrderConfirmation:

    def __init__(self, email_service):
        self.email_service = email_service

    def send_confirmation(self, order, email):
        self.email_service.send_email(email, "Order confirmation") # send email is not implemented

# class that updates inventory after purchase

class UpdateInventory:
    def __init__(self):
        remove_from_stock(self.items) # remove_from_stock is not implemented