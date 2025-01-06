#FOR-LOOP
fruits = ["apple","banana","mango"]
for x in fruits:
    print(x)
for x in "banana":
    print(x)

#FOR LOOP USING BREAK
fruits = ["apple","banana","mango"]
for x in fruits:
    print(x)
    if x=="banana":
        break

#FOR LOOP USING CONTINUE
fruits = ["apple","banana","mango"]
for x in fruits:
    print(x)
    if x=="banana":
        continue
    print(x)

#FOR-LOOP USING RANGE
for x in range(5):
    print(x)
for x in range(1,5):
    print(x)
for x in range(1,30,5):
    print(x)
    
#FOR-LOOP USING ELSE
for x in range(6):
    print(x)
else:
    print("FINISH")

#FOR-LOOP USING BREAK AND ELSE 
for x in range(6):
    if x==3: 
        break
    print(x)
else:
    print("FINISH")
 
#FOR-LOOP
classes = ["cse","aiml","ece"]
colleges = ["smsk","vbit","cbit"]
for x in classes:
    for y in colleges:
        print(x,y)
        
#FOR-LOOP     
languages = ["c", "c++", "Java", "python"]
for lang in languages:
    print(lang)
languages = ["c", "c++", "Java", "python"]
for lang in languages:
    print(lang)
    print('---------')
print("last statement")
languages = "python"
for x in languages:
    print(x)
 
#WHILE-LOOP-1 
num=1
while num<=3:
    print(num)
    num=num+1
   
#while loop-2 
num = int(input("Enter a number"))
while num!=0:
    print("You entered a", {num})
    num=int(input("Enter a number"))
print("End")

#while loop-3
age =25
while age>18:  #while True:
    print("You can vote")
    
#while loop-4
i = 1
while i<=10:
    print(i,end='\n')
    i+=1

#while loop-5
i = 1
while i<51:
    if i%5==0:
        print(i,end="\n")
    i+=1

#while loop-6
num=15
sum=0
c=15
while c<=num:
    sum=c**2+sum
    c+=1
print("The sum of squares is",sum)

#while loop-7
num=[34,12,21,55,62,38]
def prime_num(num):
    cond=0
    iter=2
    while iter <= num/2:
        if num%iter==0:
            cond=1
            break
        iter+=1
    if cond==0:
        print("prime number")
    else:
        print("not a prime number")
    for i in num:
        prime_num(1)
    
#while loop-8
number=21
count=1
print("The Multiplication table:",number)
while count<=10:
    answer=number*count
    print(number,'x',count,'=',answer)
    count+=1
    
#while loop-9
list = ['c','python','c++','java','php']
index=0
while index<len(list):
    element=list[index]
    print(len(element))
    index+=1
    
#while loop-10
count = 1
while count: print("PYTHON")
    
#while loop-11
for string in "While loop":
    if string == "0" or string == "i" or string == "e":
        continue
    print("Current String0:",string)
    
#while loop-12
for string in "Python loops":
    if string == "n":
        break
    print("Current String:",string)
    
#while loop-13
for string in "Python loops":
    pass
print("Current String:",string)

#while loop-14
n=4
for i in range(0,n):
    print(i)
    
#ACCESSING A LIST
langs=['c', 'java','python','HTML']
print(langs[0])
print(langs[3])

#NEGATIVE INDEX
langs=['c', 'java','python','HTML']
print(langs[-1])
print(langs[-3])
    
#SLICING OF A LIST
langs=['c', 'java','python','HTML']
print(langs[2:3])

l = ['p','q','r','s','t','l']
print(l[2:3])
print(l[5:])
print(l[:])

#ADDING THE ELEMENYS IN A LIST
langs=['c', 'java','python','HTML']
print("Original langs:",langs)      
langs.append('PHP')
print("Updated langs:",langs)
       
#ADDING AT SPECIFIC INDEX
langs=['c', 'java','python','HTML']
print("Original langs:",langs)      
langs.insert(2,'PHP')
print("Updated langs:",langs)

#ADD TWO LISTS
num=[1,3,5]
print("Numbers:",num)
even_num = [2,4,6]
num.extend(even_num)
print("Updated mumbers:",num)

#CHANGING THE LIST OF ITEMS
colors = ['red','pink','black']
print("Colors:",colors)
colors[2]='blue'
print("Updated colors:",colors)
    
#REMOVE ONE IOR MORE ITEMS FROM  A LIST
names = ['Ramesh','Suresh','Naresh','Mukesh','Mallesh']
del names[1]
print(names)
del names[1:4]
print(names)

#DELETION OF ENTIRE LIST
names = ['Ramesh','Suresh','Naresh','Mukesh','Mallesh']
del names
print(names)

#LENGTH OF LIST
cars = ['BMW','VOLVO','SUZUKI']
print('total cars:',len(cars))

#Iterating through a list
cars = ['BMW','VOLVO','SUZUKI']
for car in cars:
    print(car)
    
#pop
nos = [2,5,7,11]
remove_nos=nos.pop(2)
print("removed nos",remove_nos)
print("updated nos",nos)

#POP STR
cars = ['BMW','VOLVO','SUZUKI']
cars_left = cars.pop(2)
print("Original cars",cars_left)
print("Updated cars:",cars)

#COUNT OF NUMBERS
num = [2,3,4,2,5,2,7,8,9,2]
count=num.count(2)
print("Count of 2:",count)

#COUNT OF VOWELS
vowels = ['a','e','i','o','u']
count=vowels.count('e')
print("Count of i:",count)
count=vowels.count('p')
print("Count of p:",count)

#SORT
prime_num = [11,3,5,7,2]
prime_num.sort()
print(prime_num)

#SORT IN REVERSE
prime_num=[11,3.5,7,2]
prime_num.sort(reverse=True)
print(prime_num)

#SORT STRINGS
cities=["London","US","UK","China"]
cities.sort()
print("Dict orer:{cities}",cities)
cities.sort(reverse=True)
print("Cities:{cities}",cities)

#TEXT
text = ["abc","wxyz","gh","a"]
text.sort(key=len)
print(text)

#REVERSE:
sys = ["Windows","Linux","UNIX","Macros"]
print("Original list:",sys)
sys.reverse()
print("Updated list:",sys)

#COPY-1
prime_num=[2,3,5]
nums=prime_num.copy()
print("Copied list:",nums)

#COPY-2: Copied from one to another
old = [1,2,3]
new = old
new.append("a")
print("New List:",new)
print("Old List:",old)

#COPY-3
list = ['Cat',1,2,3]
new_list = list[:]
new_list.append("DOG")
print("Old list:",list)
print("New list:",new_list)
