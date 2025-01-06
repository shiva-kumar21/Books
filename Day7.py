#rindex
text = 'Python programming Python'
result = text.rindex('Python')
print(result)

#lindex 
text = 'Python programming Python'     
result = text.index('Python')
print(result)

#Creating a function
def name():
    print("Hello World")
    
#Calling a Function
def name():
    print("hello World")
name()

#AUGUMENTED
def name(surname):
    print(surname+""+"Somu")
name("Shiva")
name("Kumar")

#SQUARE NUM
def square(num):
    return num**2
obj_ = square(6)
print("The square of given num is:",obj_)

#FUNCTION-3
def a_fun(string):
    return len(string)
print("Length of a function:",a_fun("functions"))
print("length of a str:",a_fun("Strings"))

#TWO ARGUMENTS
def arithmetic_operators(num1, num2):
    sum = num1+num2
    sub = num1-num2
    mul = num1*num2
    div = num1/num2
    mod = num1%num2
    print("Sum:",sum)
    print("Sub:",sub)
    print("Mul:",mul)
    print("Div:",div)
    print("Mod:",mod)
arithmetic_operators(5,10)

#FUNCTION-4
def name(firstname,secondname):
    print(firstname+""+secondname)
name("Shiva","Kumar")

#FUNCTION WITH RETURN TYPE
def find_sqr(num):
    result = num*num
    return result
square = find_sqr(3)
print("Square:",square)

#PASS
def func():
    pass
func()

#LIBRARY FUNCTIONS
import math
square_root = math.sqrt(4)
print("square_root:",square_root)
power = pow(2,3)
print("Power:",power)

#DEFAULT FUNCTION
def msg(name,message="hello"):
    print(message,name)
msg("SMSK","College")
msg("CSE")

#KEYWORDS
def add_all(*nums):
    return sum(nums)
print(add_all(1,2,3,4))

#ARBITARY 
def name(*vehicles):                      
    print("my favourite vehicle is"+vehicles[0])
name("car","bus","cycles","scooty","bike")

#ADDER-1
def adder(x,y,z):
    print("sum:",x+y+z)
adder(10,20,30)

#ADDER-2
def adder(*num):
    sum=0
    for n in num:
        sum=sum+n
    print("Sum=",sum)
adder(3,7)
adder(1,2,3,4,5)
adder(11,10,12,13,90)

#KEYWORDS
def intro(**data):
    print("Data Types:",type(data))
    for key, value in data.items():
        print("{} is:{}".format(key,value))
intro(firstname="Shiva",lastname="Kumar",Age=18,phno=6300893654)
intro(firstname="Ram",lastname="Sita",email="ramsita21@gmail.com",country="US",phno=5852525421)

#FUNCTION-5
def name(*Student):
    print(Student[1])
name(10,20,30,40)
name("Shiva","yesh","Harish","Mouni")
    
#FUNCTION-6
def obj(n1,n2,n3):
    print("number is=",n2)
obj(n1=10,n2=20,n3=30)

#FUNCTION-7
def fun(n1,n2):
    print("Number1:",n1)
    print("Number2:",n2)
print("Without using keyword")
fun(10,20)
print("With using keyword")
fun(n2=20,n1=10)

#JOIN-1
def name(**studentnames):              
    print("Student names are"+",".join(studentnames.values()))
name(Name1="ram",Name2="Sita",Name3="Laxman")

#JOIN-2
def fun(*subject):
    print("My favourite subjects are: " + ", ".join(subject))
fun("Python", "Java", "Django", "SQL")
print("****************")

#FUNCTION-8
def name(**studentnames):              
    print("Student name is" + studentnames["Name1"])
name(Name1="ram",Name2="Sita",Name3="Laxman")

#DEFAULT VALUES
def function(subject="social"):
    print("my fav subject"+subject)
function("Hindi")
function("English")
function("Maths")
function()
function("science")

#PASSING A LIST
def function(place):
    for x in place:
        print(x)
place=["karnataka","Hyderabad","Telangana"]
function(place)

#CALL BY VALUE, REFERENCE
def testfun(arg):
    print("INSIDE FUNCTION:",id(arg))
var = "Hello"
print("ID BEFORE FUNCTION:",id(var))
testfun(var)

#RETURN VALUES
def add(x):
    return 10+x
print(add(3))
print(add(6))
print(add(5))

#AVERAGE
def avg(first,*res):
    second=max(res)
    return(first+second)/2
result = avg(40,30,50,25)
print(result)

#MARKS
def percent(c,java,**optional):
    print("c:",c)
    print("Java:",java)
    s=c+java
    for i,j in optional.items():
        print("{}:{}".format(i,j))
        s=s+j
    return s/(len(optional)+2)
result = percent(c=80,java=90,DBMS=75,python=99)
print("Percentage:",result)

#ARBITARY ARGUMENTS
def fun(*subject):                   
    print("My favourite subject is"+subject[3])
fun("Python","Java","Django","SQL")
print("****************")

#KEYWORD ARGUMENTS
def fun(a,b,c):                  
    print("my fav subject is "+b)
fun(a="Python",b="Java",c="Django")
print("*******************")

#ARBITARY KEYWORD
def fun(**subject):
    print("my fav subject is"+subject["a"])
fun(a="python",b="java",c="django")

#DEFAULT ARGUMENTS
def fun(subject="python"):
    print("my fvt subject is  ",subject)
fun("java")
fun("sql")
fun()
fun()
fun("django")