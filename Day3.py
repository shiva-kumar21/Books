#Operators
#1. Arithemetic operator
print("Arithmetic operator")
c = 10
d=20
sum = c+d
print(sum)
diff = c-d
print(diff)
mul=c*d
print(mul)
div=c/d
print(div)
floor=c//d
print(floor)
exp=c**d
print(exp)
mod=c%d
print(mod)

#2. Assignment operators
print("Assignment operator")
e = 2
f = 4
e+=f
print(e)
e-=f
print(e)
e*=f
print(e)
e/=f
print(e)
e//=f
print(e)
e%=f
print(e)
e**=f
print(e)
e=int(e)
print(e)
e>>=1
print(e)
e<<=1
print(e)
e^=1
print(e)

#3. COMPARISON OPERATOR
print("Comparison operator")
a = 20
b = 30
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)

#4. LOGICAL OPERATORS
print("Logical operators")
x = 10
print(x<5 and x<10)
print(x<5 or x<10)
print(not(x<5 and x<10))

#5. IDENTITY OPERATORS
print("Identity operators")
a = b =10
print(a is b)
print(a is not b)

x = ["Dog","Cat"]
y = ["Dog","Cat"]
z=["Dog","Pig"]
print(x is z)
print(y is z)
print(x is not z)
print(x==y)

#6. Membership operators
print("Membership operators")
x = [10,20,30]
print(10 in x)
print(21 in x)
print(10 not in x)
print(21 not in x)

msg = "Hi, This is Shiva"
dict = {1: 'a', 2:'b'}
print('H' in msg)
print('Is'in msg)
print('Shiva' not in msg)
print('a' in dict)
print(2 in dict)

#7. Bitwise Operators
print("Bitwise operators")
a=2
b=6
print("a:",a,"b:",b,"a&b:",a&b)
print("a:",bin(a))
print("b:",bin(b))
print("a:",a,"b:",b,"a|b:",a|b)
print("a:",bin(a))
print("b:",bin(b))
print("a:",a,"b:",b,"a^b:",a^b)
print("a:",bin(a))
print("b:",bin(b))
print("a:",a,"b:",b,"~a:",~a)
print("a:",bin(a))
print("b:",bin(b))
print("a:",a,"b:",b,"a<<2:",a<<2)
print("a:",bin(a))
print("b:",bin(b))
print("a:",a,"b:",b,"a>>2:",a>>2)
print("a:",bin(a))
print("b:",bin(b))

#CONTROL STATEMENTS

#SEQUENTIAL C.S
print("Hello, This is Shiva")
print("This is a sequential control statement")

#SELECTION C.S
#IF STATEMENT
print("IF STATEMENT")
a=200
b=300
if a<b:
    print("a is less than b")

#ELIF STATEMENT
print("ELIF STATEMENT")
c=200
d=200
if c<d:
    print("c is less than d")
elif c==d:
    print("c and d are equal",)
    
#IF-ELSE STATEMENT
print("IF-ELSE STATEMENT")
e=200
f=300
if e<f:
    print("e is less than f")
else:
    print("e is greater than f")
    
#Nested-if STATEMENT
print("Nested-If")
x =21
if x>10:
    print("above 10")
    if x>20:
        print("and also above 20")
    else:
        print("but not above 20")

#SHORTCUT OR SHORTHAND
a = 2
b =900
print("A") if a>b else print("B")

#Check different logical conditions: AND, OR, and NOT.
a = 20
b = 30
c = 900
if a>b and c>a:
    print("And condition is satisfied")
if a>b or c>a:
    print("Or condition is satisfied")
if not a>b:
    print("a is not greater than b")
    
# Assign result based on marks: Fail, Pass, or Distinction.
marks = 40
result = ""
if marks<35:
    result="FAIL"
elif marks>75:
    result="Passed with distinction"
else:
    result="Pass"
print(result)

# Check if the number is even or odd using an else statement.
num = int(input("Enter the number:\n"))
if num%2==0:
    print("Even")
else:
    print("Odd")
    
#Check if the user is eligible for voting based on age using an else statement.
age = int(input("Enter your age:\n"))
if age>18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")
    
#Determine the largest number among a, b, and c using conditional statements.
a = int(input("Enter a:\n"))
b = int(input("Enter b:\n"))
c = int(input("Enter c:\n"))
if a>b and a>c: # elif a>b and a>c
    print("a is largest")
if b>a and b>c: #elif b>a and b>c
    print("b is largest") 
if c>a and c>b: #elif c>a and c>b
    print("c is largest")

#Assign input and check if the number matches specific values (10, 50, or 100) using elif.
num = int(input("Enter a num:\n"))
if num == 10:
    print("num=10")
elif num==50:
    print("num=50")
elif num==100:
    print("num=100")
else:
    print("num=10 or 50 or 100")
    
# Check the range of marks and print the corresponding grade using elif
marks = int(input("Enter your marks:\n"))
if(marks>=80 and marks<=100):
    print("Grade A+:Congrats!")
elif(marks>=50 and marks<=80):
    print("Grade B:Second place")
elif(marks>=40):
    print("Grade C:Pass")
    
#password
name = input("Enter a name:\n")
password = input("Enter a password:\n")
if name == "Python":
    if password == "Shiva_121":
        print("Both inputs are correct!")
    else:
        print("inputs are incorrrect!")
else:
    print("The name & password are wrong...")
    
