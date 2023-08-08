from Person import Person
from StudentClass import Student
from Teacher import Teacher

def main():
    Sulaiman = Person("Sulaiman Al-Farsi", 23)
    print(Sulaiman.get_name())
    
    
    Sulaiman.set_name("Sulaiman alfarsi")
    print(Sulaiman.get_name())
    print(Sulaiman.descrip())
    
    Sulaiman.run()
    Sulaiman.laugh()
    
    pesron2 = Person("Yahya", 22)
    pesron2.laugh()
    print(pesron2.descrip())
    
    student1 = Student("Ahmed", 20,2020)
    student2 = Student("Saif", 21,2021)
    
    print(student1.say_hi())
    print(student2.say_hi())
    
    t1 = Teacher("Ali",45,2020)
    print(t1.say_hi())
    

main()