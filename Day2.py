#ASSIGNING VALUES TO VARIABLES

#BASIC FORM
str="Shiva"
print(str)

#TUPLE ASSIGNMENT
X,Y = (50,100)
print('X=',X)
print('Y=',Y)

#SEQUENCE ASSIGNMENT
a,b,c,d,e='SHIVA'
print(a,b,c,d,e)

#EXTENDED SEQUENCE ASSIGNMENT
i,*j,k = "Classes"
print(k) 

#MULTIPLE TARGET ASSIGNEMNET
a=b=c=21
print(c)

#AUGUMENTED ASSIGNMENT
s = 20
s+=1
print(s)

#INPUT AND OUTPUT
r = input("Enter your name:")
print(r)

a=input("Enter your name:\n")
b=input("Enter your college name:\n")
c=input("Enter your branch:\n")
d=int(input("Enter your pin:\n"))

#TYPES
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))

#DATATYPES
value=10
print(type(value))

value=21.00
print(type(value))

value=10+20j
print(type(value))

value="Shiva"
print(type(value))

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
e = 5.0
f = 10
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
