#DICTIONARY-1
clgs = {"Samskruti": "smsk", "Vignanbharati":"vbit","MallaReddy":"mrec"}
print(clgs)

#DICTIONARY-2
#my_dict = {1:"One",2:"Two",3:"Three"}
#my_dict = {(1,2):"One Two",3:"Three"}
my_dict = {1:"hello",(1,2):"Hi Hello"}
#my_dict = {"USA":["California","Chicago","New York"]}

#DICTIONARY-3
depts = {"cse":"computer science","ece":"electronics","aiml":"Artificial Intelligent/Machine Learning"}
print(depts)

#ACCESS DICTIONARY
depts = {"cse":"computer science","ece":"electronics","aiml":"Artificial Intelligent/Machine Learning"}
print(depts["aiml"])
print(depts["ece"])

#ADD THE DICTIONARIES
depts = {"cse":"computer science","ece":"electronics","aiml":"Artificial Intelligent/Machine Learning"}
depts["IT"]="Information Technology"
print(depts)

#REMOVE THE DICTIONARIES
depts = {"cse":"computer science","ece":"electronics","aiml":"Artificial Intelligent/Machine Learning"}
del depts["aiml"]
print(depts)

#CLEAR
depts = {"cse":"computer science","ece":"electronics","aiml":"Artificial Intelligent/Machine Learning"}
depts.clear()
print(depts)

#CHANGE
depts = {"cse":"computer science","ece":"electronics","aiml":"Artificial Intelligent/Machine Learning"}
depts["aiml"] = "MACHINE LEARNING"
print(depts)

#ITERATION
departments = {"cse":"computer science","ece":"electronics","aiml":"Artificial Intelligent/Machine Learning"}
for dept in departments:
    print(dept)
print()
for dept in departments:
    depts = departments[dept]
    print(depts)
    
#LENGTH OF DICTIONARY
depts = {"cse":"computer science","ece":"electronics","aiml":"Artificial Intelligent/Machine Learning"}
print(len(depts))
colleges = {}
print(len(colleges))

#POP
marks = {"C":99,"Java":78,"Python":10}
elements = marks.pop("Java")
print("Popped marks:",elements)
print("The dict is:",marks)

#UPDATE
marks = {"C":99,"Java":78,"Python":10}
internal_marks = {"Practical":66}
marks.update(internal_marks)
print(marks)

#KEYS-1
marks = {"C":99,"Java":78,"Python":10}
dictkeys = marks.keys()
print(dictkeys)
#KEYS-2
employee = {"name":"Shiva","age":18,"empid":121}
dict_keys = employee.keys()
print(dict_keys)

#VALUES
marks = {"C":99,"Java":78,"Python":10}
dictkeys = marks.values()
print(dictkeys)

#GET()-1
marks = {"C":99,"Java":78,"Python":10}
result = marks.get("C")
print(result)

#GET()-2
std = {"name":"Shiva","age":18,"std_score":89}
print("name",std.get("name"))
print("age",std.get("age"))
print("std_score",std.get("std_score"))
print("marks",std.get("marks"))
print("marks",std.get(0.0))

#POP ITEM
std = {"name":"Shiva","age":18,"std_score":89}
result = std.popitem()
print("return value=",result)
print("std=",std)
std['profession'] ="Software"
print("return value=",result)
print("std=",std)

#COPY-1
Original_marks = {"Physics":66,"c":89,"java":45}
copied_marks = Original_marks.copy()
print("Original marks:",Original_marks)
print("Copied marks:",copied_marks)

#COPY-2
original = {1:"One",2:"Two"}
new=original
print("Original:",original)
print("new:",new)

#MEMBERSHIP
file_types = {"txt":"text file","pdf":"Document file","jpg":"Image file"}
print("pdf" in file_types)
print("mp3" in file_types)
print("mp3" not in file_types)

#EMPLOYEE DETAILS
employee = {"Name":"Shiva","age":18,"salary":20000,"Company_name":"IBM"}
print(type(employee))
print("Employee Details:")
print(employee)

#SORT
dict = {1:"Mukesh",2:"Vikesh",3:"Gukesh"}
print(sorted(dict))

#ANY
dict = {1:"Mukesh",2:"Vikesh",3:"Gukesh"}
print(any({":",":",":"}))

#ALL
dict = {1:"Mukesh",2:"Vikesh",3:"Gukesh"}
print(all({":",":",":"}))

##########STRINGS
str1 = "Python Programming"
str2 = "python"
print(str1,str2)

#ACCESS STRINGS
name = "python"
print(name[1])

#NEGATIVE ACCESS
name = "python"
print(name[-4])

#SLICING
name = "python"
print(name[1:4])
print(name[:])
print(name[1:])
print(name[:4])
print(name[-1:-4])
print(name[-1:4])

#MULTIPLIER
message =""" Hi Students! Welcome to my class. I hope you are satisfied with my session. thank you for your valuable time..."""
print(message)

#COMPARE
str1 = "Python Program"
str2 = "Python programming"
str3 = "Python program"
print(str1==str2)
print(str1==str3)

#JOINT
Greet = "Hello"
name = "Python"
result = Greet+name
print(result)

#ITERATION
Greet = "Hello"
for letter in Greet:
    print(letter)
    
#LENGTH
Greet = "hello"
print(len(Greet))
    
#MEMBERSHIP
print("H" in "Program")
print("P" in "Program")
print("g" not in "Program")

#UPPER
msg = "Python is fun"
print(msg.upper())

#LOWER
msg = "Python is FUN"
print(msg.lower())

#PARTITION
str = "Python is fun"
print(str.partition('is'))
print(str.partition('not'))
str = "Python is fun, isn't it?"
print(str.partition('is'))

#SPLIT()-1
str = "Python is fun"
print(str.split())

#SPLIT()-2
spl ="I Love Python"      #CODE ERROR
print(spl.split("is"))
spl2 = 'cse','ece','aiml'
print(spl2.split("#",1))
print(spl2.split("#",0))

#REPLACE-1
text = 'bat ball'
replaced_text = text.repalce('ba','ro')
print(replaced_text)

#REPLACE-2
song = 'ba,baba sheep'
print(song.replace('ba','babaaa'))
song = 'let it be, let it be, let it be'
print(song.replace('let',"don't let",2))

#FIND
message = "Python is a fun programming lang"
print(message.find("fun"))
message = "Python is a fun programming lang"
result = message.index('is')
print(result)
print(message.index('ing',10))
print(message.index('fun',10,-4))
message = "Python is fun"
result = message.index('is fun')
print("substring 'is fun':",result)

#rstrip
title = "Python Proramming   "
result = title.rstrip()
print(result)

#rstrip
Ranstr = "This is good    "
print(Ranstr.rstrip())
print(Ranstr.rstrip('si oo'))
print(Ranstr.rstrip('sid oo'))

#split()
grocery = 'MILK#CHICKEN#BREAD#BUTTER'
print(grocery.split('#',1))
print(grocery.split('#',2))
print(grocery.split('#',5))
print(grocery.split('#',0))

#startswith()-1
mes = 'Python is fun'
print(mes.startswith('Python'))

#startswith()-2
text = 'Python is easy to learn.'
result = text.startswith('is easy')
print(result)
result = text.startswith('Python is')
print(result)
result = text.startswith('Python is easy to learn.')
print(result)

#startswith()-3
text = 'Python is easy to learn.'
result = text.startswith("Python is",8)
print(result)

#isnumeric()
pin = '1234'
print(pin.isnumeric())
nums = "Python3"
print(nums.isnumeric())

#isdigit()
str1 = "890"
print(str1.isdigit())
str2 = "python"
print(str2.isdigit())
name1 = "Python3"

#isalnum()
print(name1.isalnum())
name2 = "Python 3"
print(name2.isalnum())
s = "23456"

#isdecimal()
print(s.isdecimal())
s1 = "2345lab"
print(s1.isdecimal())

      





