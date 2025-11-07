import uuid


class Items:
    def __init__(self, item_name, price, amount, ID):
        self.item_name = item_name
        self.price = price
        self.amount = amount
        self.ID = ID
    
    def discount(self, discount):
        return self.price - (self.price * (discount/100))
    
    def getitemname(self):
        return self.item_name
    
    def getprice(self):
        return self.price
    
    def getamount(self):
        return self.amount

    def getID(self):
        return self.ID 


def createID():
    return uuid.uuid4()


test_item = Items('Windows 11 pro key', 124.99, 100, createID())
    
    