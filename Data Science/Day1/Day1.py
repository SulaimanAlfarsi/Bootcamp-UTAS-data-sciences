class Person:
    #Constructor to create Objects
    #intializeinstance varibles
    def __init__(self, name, p_age):
        self.name = name
        self.age = p_age
        #use term ogf encapsualtion
        #accessor methods
    def get_name(self):
        return self.name 
    def get_age(self):
        return self.age
        #setter / mutotur methods 
    def set_name(self,newName):
        self.name = newName
    def set_age(self,newAge):
        self.age = newAge

    def descrip(self):
        return f"Person name {self.name} is {self.age} years old"
    
    def run(self):
        print(self.name, "is runing")
        
    def laugh(self):
        print(self.name, "say Hi")
