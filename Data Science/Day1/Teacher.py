from Person import Person
class Teacher(Person):
    def __init__(self,name,age,year):
        super().__init__(name,age)
        self.exp_year = year
    def say_hi(self):
        return f"Hello {self.name} as Teacher"