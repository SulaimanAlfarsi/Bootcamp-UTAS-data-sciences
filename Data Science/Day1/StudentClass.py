from Person import Person
class Student(Person):
    #constructor
    def __init__(self,name,age,year):
        super().__init__(name,age)
        self.acadmic_year = year
    def say_hi(self):
        return f"Hello {self.name} as student"
    