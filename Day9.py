class student:
    count = 0  
    def __init__(self):
        self.name = str(input("Enter your name: "))
        self.rollno = input("Enter the roll number: ")
        if self.rollno.isdigit():
            self.rollno = int(self.rollno)
        else:
            print(f"Invalid roll number entered: {self.rollno}. Please input a valid roll number.")
            self.rollno = 0  
    def details(self):
        print("Name:", self.name, "Roll No:", self.rollno)
        student.count += 1  
s1 = student()
print("-------------")
s2 = student()
print("-------------")
s3 = student()  
print("-------------")
s4 = student()
print("Total number of students:", student.count)

# Multilevel inheritance: Animal -> Dog -> Cat
class animal:
    def speak(self):
        print("Animal is speaking")
class dog(animal):
    def bark(self):
        print("Dog is barking")
class cat(dog):
    def meow(self):
        print("Cat is meowing")
c=cat()
c.bark()
c.speak()
c.meow()

# Derived-class calling base-class method
class parent:
    def parent_method(self):
        print("Calling parent parentmethod")
class child(parent):
    def child_method(self):
        print("Calling childmethod")
c=child()
c.child_method()
c.parent_method()

# Base class for division
class division:
    def __init__(self, a, b):
        self.n = a
        self.d = b  
    def divide(self):
        return self.n / self.d 
class modulus:
    def __init__(self, a, b): 
        self.n = a
        self.d = b
    def mod_divide(self):
        return self.n % self.d 
class div_mod(division, modulus):
    def __init__(self, a, b):
        division.__init__(self, a, b)  
        modulus.__init__(self, a, b)       
    def div_mod(self):
        divval = self.divide()  
        modval = self.mod_divide()  
        return divval, modval  
x = div_mod(10, 2)
print("Division:", x.divide())
print("Modulus Division:", x.mod_divide()) 
print("Div and Mod Results:", x.div_mod())  

# Multiple inheritance example for sum, multiplication, and division
class calculation1:
    def sum(self,a,b):
        return a+b;
class calculation2:
    def mul(self,a,b):
        return a*b;
class derived(calculation1,calculation2):
    def divivde(self,a,b):
        return a/b;
d=derived()
print(d.sum(10,2))
print(d.mul(4,2))
print(d.divivde(22,4))

# Hierarchical inheritance example: Car -> Bike, Scooty
class car:
    def bmw(self):
        print("car colour is black")
class bike(car):
    def kawasaki(self):
        print("bike colour is Green")
class scooty(car):
    def pept(self):
        print("scooty colour is blue")
a=scooty()
a.pept()
a=bike()
a.kawasaki()
a=car()
a.bmw()

# Using super() to call the parent class constructor
class parentsDemo:
    def __init__(self,msg):
        self.message=msg
    def showmessage(self):
        print(self.message)
#child class
class childDemo(parentsDemo):
    def __init__(self,msg):
        super().__init__(msg)
#object
obj=childDemo("welcome to smsk........")
obj.showmessage()

#Polymorphism:
class baseclass1:
    def A(self):
        print("this is base class 1")
class baseclass2:
    def A(self):
        print("this is baseclass2")
class baseclass3:
    def A(self):
        print("this is base class3")
def poly(obj):
    obj.A()
obj1=baseclass1()
obj2=baseclass2()
obj3=baseclass3()
poly(obj1)
poly(obj2)
poly(obj3)

#Method overloading
class A:
    def add(self, a, b, c=None):  
        if c is not None:
            return a + b + c  
        else:
            return a + b  
obj = A()
print(obj.add(2, 4))  
print(obj.add(1, 2, 3)) 

# Method overriding example: Child class overrides parent class method
class parent:
    def vechiles(self):
        print("this is my bike")
class child(parent):
    def vechiles(self):
        print("this is my car")
obj=child()
obj.vechiles()

#Using multipledispatch
from multipledispatch import dispatch # type: ignore
class A:
    @dispatch(int, int)
    def add(self, a, b):
        return a + b    
    @dispatch(float, float, float)
    def add(self, a, b, c):
        return a + b + c 
    @dispatch(str, str)
    def add(self, a, b):
        return a + b
obj = A()
print(obj.add(1, 2))  
print(obj.add(1.54, 3.45, 2.67))  
print(obj.add("python", "program"))  

#MONEY
def pocket_money_cal(no_of_weeks):
    total_pocket_money = 0
    for i in range(1,no_of_weeks+1):
        user_weekly_pocket_money = int(input(f"Enter {i} week pocket money"))
        total_pocket_money += user_weekly_pocket_money
    return total_pocket_money
no_of_weeks = int(input("Enter the no.of weeks to calculate the pocket money:-"))
calculated_pocket_money = pocket_money_cal(no_of_weeks)
print(f"Total pocket money of{no_of_weeks} weeks is Rupees {calculated_pocket_money}/-")
 
























