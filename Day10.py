#ENCAPSULATION
class Computer:
    def __init__(self):
        self._maxprice = 900
    def sell(self):
        print("Selling Price: {}".format(self._maxprice))
    def  setMaxprice(self,price):
        self._maxprice = price
c = Computer()
c.sell() 
c.self_maxprice=1000
c.sell()
c.setMaxprice(1000)
c.sell()

#FILE HANDLING
f = open("details.txt",'r')
content=f.read()
print(content)
f.close()

#DATA GETTING FROM 
f = open("Details.txt",'a')
content=f.write("I am from CSE")
print(content)
f.close()
f=open("Details.txt",'r')
content=f.read()
print(content)
f.close()

#APPEND
f = open("Details.txt",'a')
content=f.write("I am from CSE")
print(content)
f.close()
f=open("Details.txt",'r')
content=f.read()
print(content)
f.close()

#WRITE
a = open("abc.txt",'w')
a.write("Welcome to my python\n")
a.close()

#READ
a = open("abc.txt","r")
print(a.read())
a.close()

#ABSTACTION
#ABSTRACT CLASS:
from abc import ABC
class polygon(ABC):
    #abstact  class method
    def sides(self):
        pass
class Triangle(polygon):
    def sides(self):
        print("Triangle has 3 sides")
class Pentagon(polygon):
    def sides(self):
        print("Pentagon has 5 sides")
class Hexagon(polygon):
    def sides(self):
        print("Hexagon has 6 sides")
class Square(polygon):
    def sides(self):
        print("Square has 4 sides")
t=Triangle()
t.sides()
s=Square()
s.sides()
p=Pentagon()
p.sides()
H=Hexagon()
H.sides()
p1=polygon()
p1.sides()

#OPEN A FILE
f =open("abc.txt","wb")
print("CSE",f.name)
print("Close a file",f.close)
#print("Opening mode",f.mode)
#f.mode()
f.close()

#READING A FILE
with open("abc.txt","r") as file:
    content=file.read()
    print(content)
    
#READLINE
with open("abc.txt","r") as file:
    line=file.readline()
    while line:
        print(line, end='')
        line=file.readline()
        
#WRITE
with open("abc.txt","w") as file:
    file.write("Hello CSE!")
    print('Content-------')
    
#USING FOR LOOP-1
a=["Hello\n","Coders\n","CSE\n"]
f1=open("myfile.txt",'w')
f1.writelines(a)
f1.close()
f1=open("myfile.txt",'r')      
lines=f1.read()
count=0
for line in lines:
    count+=1
    print("Lines{}:{}".format(count,lines.strip()))
    
#USING FOR LOOP-2
a=["Hello\n","Coders\n","CSE\n"]
f1=open("myfile.txt",'w')
f1.writelines(a)
f1.close()
f1=open("myfile.txt",'r')      
lines=f1.readlines()
count=0
for line in lines:
    count+=1
    print("Lines{}:{}".format(count,lines))

#ARRAYS
import array as ar
a = ar.array('f',[1.1,2.8,9.9])
print(a)
a = ar.array('i',[2,3,4])
print("First ele:",a[0])
print("Second ele:",a[1])
print("Third ele:",a[2])

#SLICING USING ARRAYS
import array as arr
num_list=[2,5,6,8,99,89,77,56,34,66]
num_array=arr.array('i',num_list)
print(num_array[2:5])
print(num_array[:-5])
print(num_array[:])
print(num_array[5:])

#CHANGING
import array as ar
nums = arr.array('i',[1,2,3,4,5])   
nums[0]=0
nums[2:3]=arr.array('i',(6,7,8))
print(nums)

#APPEND
import array as ar
odd = arr.array('i',[1,3,5])   
even=arr.array('i',[2,4,6])
nums=arr.array('i')
nums=odd+even
print(nums)

#DELETE
import array as ar
n = arr.array('i',[1,2,3,4,5])   
del n[2]
del n
print()

#ARRAYS USING STRINGS
months = ["jan","feb","mar","apr","may","jun"]
print(months[5])
months[3]="apr"
print(months)
print(len(months))
months.append("Aug")
print(months)
months.insert(1,"sep")
print(months)
months.remove("may")
print(months)
     
#COMBINE
l1 = ["cse","ece","eee"]  
l2 = ["ai&ml","PT"]
com_list = l1+l2
print(com_list)

#CREATE DIFFERENT ARRAYS
import array
int_array=array.array('i',[1,2,3,4])
float_array=array.array('f',[1.1,2.2,3.3,4.4])
unicode_array=array.array('u',['\u2167','\u007D'])
print(int_array)
print(float_array)
print(unicode_array)
print(type(unicode_array))

#for
import array 
int_array = array.array('i',[1,2,3,4])
for a in int_array:
    print(a)
    
#REVERE OF AN ARRAY
import array 
int_array = array.array('i',[1,2,3,4])
int_array.reverse()
print(int_array)

#OCCURENCCE
import array 
int_array = array.array('i',[1,2,3,4,1,1,2])
print(int_array.count(1))
print(int_array.count(3))

#Convert array to list:
int_array = array.array('i',[1,2,3,4])
print(int_array.tolist())

#LIST
l=list(range(10))
print(l)
l1=l+["one","Two","Three"]
print(l1)
    
#ROCK, PAPER, SCISSORS
import random
print("Winning Rules:"+"rock vs paper -> paperwins\n"+"rock vs scissors -> rockwins\n"+"paper vs scissors -> paperwins\n")
while True:
    print("Enter your choice:\n-1.Rock\n 2.Paper\n 3.Scissors\n")
    choice=int(input("Enter your choice"))
    while choice>3 or choice<1:
        choice=int(input("Enter valid"))
    if choice==1:
        choice_name='Rock'
    elif choice==2:
        choice_name='Paper'
    else:
        choice_name='scissors'
    print('user choice is',choice_name)
    print("Now computer choice")
    computer_choice=random.randint(1,3)
    if computer_choice==1:
        computer_choice_name='Rock'
    elif computer_choice==2:
        computer_choice_name='Paper'
    else:
        computer_choice_name='Scissors'
    print("Computer choice:",computer_choice_name)
    print("choice,'vs',computer_choice_name")
    if choice==computer_choice:
        result="DRAW"
    elif (choice==1 and computer_choice==2) or (computer_choice==1 and choice==2):
        result="Paper"
    elif (choice==1 and computer_choice==3) or (computer_choice==1 and choice==3):
        result="Rock"
    elif (choice==2 and computer_choice==3) or (computer_choice==2 and choice==3):
        result="Scissors"
    if result=="DRAW":
        print("It is tie")
    elif result==choice_name:
        print("You are win")
    else:
        print("Computer wins")
    print("do u want to play again")
    ans =input().lower()
    if ans=='n':
        break
    print("Thanks for replying")
    
    