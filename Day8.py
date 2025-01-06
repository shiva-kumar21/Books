#LAMBDA
value = lambda a:a+10
print(value(5))

#LAMBDA USING FUNCTIONS
x = lambda a,b:a*b
print(x(10,20))

#LAMBDA USING ONE OR MORE VALUES
value = lambda a,b,c:(a*b)/c
print(value(10,20,30))

#LAMBDA USING STRINGS
x = lambda string: string in "Python"
print(x("P"))
print(x("g"))

#LAMBDA USING FILTER
num = [10,20,30,40]
greater = list(filter(lambda num:num>25,num))
print(greater)

#LAMBDA USING LIST
list_ = [32,44,8,89,90,77]
odd_list = list(filter(lambda num:(num%2!=0),list_))
print("Odd numbers",odd_list)

#SQUARE ROOT USING LAMBDA
sqr = [lambda n=n:n**2 for n in range(0,11)]
for square in sqr:
    print("sqr of 0-10:",square(),end="")

#IDENTIFYING MINIMUM NUMBER USING LAMBDA
min = lambda x,y:x if(x<y) else y
print("\nGreater Number:\n",min(35,96))

#RECIPROCAL AND LAMBDA
def reciprocal(num):
    return 1/num
lambda_reciprocal = lambda num:1/num
print("Def keyword:",reciprocal(6))
print("Lambda Keyword:",lambda_reciprocal(6))

#FIND THIRD LARGEST
my_list = [[3,4,5,6],[23,45,99,12,9],[5,6,7,8,9]]
sort_list = lambda num:(sorted(n) for n in num)
third = lambda num,func:[l[len(l)-2] for l in func(num)]
result = third(my_list,sort_list)
print("Third largest:",result)

#MAP-1
num = [1,9,5,3,7,10,8,4]
greater = list(map(lambda num:num*2,num))
print(greater)

#MAP-2
actions = ['eat','sleep','read']
result = list(map(list,actions))
print(result)

#MAP-3
def mul(i):
    return i*i
x = map(mul,(3,5,7,11,13,14))
print(x)
print(list(x))

#A LOOP WITH USING MAP-4
number = [1,2,3,4,5]
mul=[]
for n in num:
    mul.append(n**2)
print(mul)

#WITHOUT USING MAP-5
def mul(i):
    return i*i
num=(1,2,3,4,5)
res = map(mul,num)
print(res)
mul_op = list(res)
print(mul_op)

#LENGTH
msg = ["Welcome","to","Python","Class"]
x = list(map(len,msg))
print(x)

#MATH.SQRT
import math
num=[9,36,49,81,121]
x=list(map(math.sqrt,num))
print(x)

#MAP USING LAMBDA
num = (6,9,21,77)
res=map(lambda i:i+1,num)
print(list(res))

#MAP WITH TUPLE FOR UPPER
def exp(s):
    return s.upper()
tuple_exp=('i','love','python')
updated_tuple = map(exp,tuple_exp)
print(updated_tuple)
print(tuple(updated_tuple))

#MAP WITH TUPLE FOR LOWER
def exp(s):
    return s.lower()
tuple_exp=('i','LOVE','python')
updated_tuple = map(exp,tuple_exp)
print(updated_tuple)
print(tuple(updated_tuple))

#USING DICTIONARY
car = {1:"BMW",2:"BENZ",3:"FERRARI"}
car = dict(map(lambda x:(x[0],x[1]+'i'), car.items()))
print("Modified cars:",car)

#USING SET
def ex(i):
    return i%3
set_ex = {33,102,62,96,44,28}
upd_items = map(ex,set_ex)
print(upd_items)
print(set(upd_items))

#LAMBDA
x = lambda a,b:a+b
print(x(10,5))
y = lambda a:a+10
print(y(12))
print((lambda a,b:a+b)(10,5))
print((lambda a,b,c,d:((a+b)*c/d)(4,8,2,10)))
print((lambda a,b=10,c=5:(a+b)*c)(2))
x = lambda string:string not in "Python Programming"
print(x("j"))
print(x("P"))
num=[6,7,4,9,2,3,8]
even=print("Even numbers are",(tuple(filter(lambda num:num%2==0,num))))
odd = print("Odd numbers are",(list(filter(lambda num:num%2==1,num))))

num=[12,87,63,26,45,98,32,11,577,66]
greater =print("Greater than 50 numbers are",(set(filter(lambda num:num>50,num))))
lesser=print("Lesser than 50 numbers are",(set(filter(lambda num:num<50,num))))

num = [6,7,4,9,2,3,8]
twice = print(list(map(lambda num:num*2,num)))
thrice=print(list(map(lambda num:num*3,num)))

x = lambda *args:sum(args)
print(x(6,7,4,9,2,3,8))

####CLASS AND OBJECT
#C&O-1
class add:
    a=10
p1=add()
print(p1.a)

#C&0-2
class person:
    colour = "fair"
    height = 5.8
    def run(self):
        print("running")
obj=person()
print(obj.colour,obj.height)
obj.run()

#C&O-3
class bike:
    name = ""
    color = 0
bike1 = bike
bike1.color="blue"
bike1.name="R15"
print(f"Name:{bike1.name},color:{bike1.color}")

#C&O-4
class student:
    Student_id=0
Student1=student()
Student2=student()
Student1.StudentID=123456 
print(f"StudentID: {Student1.StudentID}")
Student2.StudentID=1234567
print(f"StudentID: {Student2.StudentID}")

#C&O-5
class Dog:
    sound ="bark"
dog1=Dog()
print(dog1.sound)
        
#INIT()
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1 = student("Ram",25)
print(s1.name)
print(s1.age)
s2 = student("Yesh",17)
print(s2.name)
print(s2.age)
s3 = student("Shiva",18)
print(s3.name)
print(s3.age)

#ATTRIBUTES AND METHODS
class room:
    leng=0.0
    breadth=0.0
    def cal_area(self):
        print("Area of room",self.leng*self.breadth)
study_room=room()
study_room.leng=44.2
study_room.breadth=99.90
study_room.cal_area()

#ATT&METHOD-2
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
person1=person("Ramesh",25)
person2=person("Suresh",45)
print(person1.name)
print(person2.age)

#SELF PARAMETER
class person:
    def __init__(obj,name,age):
        obj.name=name
        obj.age=age
    def myfun(abc):
        print("Hello my Nme is"+abc.name)
p1=person("Shiva",18)
p1.myfun()

#MODIFY
class person:
    def __init__(obj,name,age):
        obj.name=name
        obj.age=age
    def myfun(abc):
        print("Hello my Name is"+abc.name)
p1=person("Shiva",17)
p1.age="18 years"
print(p1.age)

#DELETE
class person:
    def __init__(obj,name,age):
        obj.name=name
        obj.age=age
    def myfun(abc):
        print("Hello my Nme is"+abc.name)
p1=person("Shiva",18)
del p1.age