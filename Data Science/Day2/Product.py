#create Product class,
#each product has name , category ,and price --> instance varibale
#class is able to return a discription of product --> method
#for each product be able to compare discount of a given amount
#(compute price after discount of amount)

class Product:
    def __init__(self, name , category , price):
        self.name = name
        self.category = category
        self.price = price
        
    def getName(self):
        return self.name
    
    def getCategory(self):
        return self.category
    
    def getPrice(self):
        return self.price
    
    def setName(self,newName):
        self.name = newName
    
    def setcategory(self,newcategory):
        self.category = newcategory
    
    def setprice(self,newprice):
        self.price = newprice
        
        
    
    def descrip(self):
        return f" name: {self.name} category: {self.category}  price: {self.price}"
    
    
    def discount(self, amount):
        self.price = self.price - (self.price * amount/100)
        if self.category == "phone":
            self.price += 10
    
    
        
    
    