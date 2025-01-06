#tuple
num=(1,2,3)
print(num)

#CREATE A TUPLE
smsk = ()
print(smsk)

#TYPES OF TUPLES
names = ('smsk','klu','vbit','bids')
print(names)
float_values=(1.2,2.3,9.8)
print(float_values)

#MIXED  TUPLES
mixed_tuple = (222,'hello','Python')
print(mixed_tuple)

#ACCESSING A TUPLE
langs = ('Python','C','Java','C++')
print(langs[0])
print(langs[2])

#MODIFIED:Unchanchable
langs = ('Python','C','Java','C++')
langs[1] = 'C'
print(langs)

#LENGTH
langs = ('Python','C','Java','C++')
print('langs:',len(langs))

#ITERATION THROUGH TUPLE
langs = ('Python','C','Java','C++')
for lang in langs:
    print(langs)
    
#CHECKING
colors = ["red","black","yellow","white"]
print("blue" in colors)
print("white" in colors)

#DELETE
animals = ["cat","rat","dog"]
print(animals)
del animals

#CHANGE: Immutable
animals = ["cat","rat","dog"]
animals[1] = "Pig"
print(animals)

#READ A TUPLE
single_tuple =  ("Tuple")
print(type(single_tuple))
single_tuple1 = ("Tuple",)
print(type(single_tuple1))
single_tuple2 = "Tuple",
print(type(single_tuple2))

#SLICING 
fruits = ("Apple","Banana","Mango","Orange","Grapes")
print("Elements at -1 index:",fruits[-1])  #POSITIVE SLICING
print("Elements between 1 and 3 index:",fruits[1:3])
print("Elements between 0 index:",fruits[0])

#REPETITION
tuple_ = ('Python','Tuples')
print('Original tuples:',tuple_)
tuple_ = tuple_*3
print('New tuples:',tuple_)

#COUNT
t1 = (0,1,2,3,5,6,3,2,4,7,8,2,3,9,0,2,3,2,2)
t2 = ("Python","C","C++","Python","Java",)
res = t1.count(2)
print("count of 2 in t1:",res)
res = t2.count("Python")
print("count of python:",res)
res = t2.count("C")
print("count of C:",res)

#index 
tt = (0,1,2,3,2,3,1,3,2)
res = tt.index(3)
print("first occurence:",res)

#MEMBERSHIP
tuples_ = ("Python","tuple","Ordered","Mutable","Immutable")
print("tuple" in tuples_)
print("items" in tuples_)
print("Immutable" not in tuples_)
print("items" not in tuples_)

#ITERATING
tuples_ = ("Python","tuple","Ordered","Mutable")
for items in tuples_:
    print(items)
    
#ADDING THE TUPLES
tuples_ = ("Python","tuple","Ordered","Mutable")
print(tuples_+(4,5,6))

#GENERAL PROGRAM-1
tuple1 = ("Shiva","SMSK","CSE")
tuple2 = ("A","B","C")
print(tuple1,"\n",tuple2)

#SETS
std_id = {111,112,113,114,115}
print('std_id:',std_id)
vowel_letters = ('a','e','i','o','u')
print('vowels:',vowel_letters)
mixed_sets = {1,'hello', '-404',}

#EMPTY SET
empty_set = set()
empty_dict = {}
print('Datatype of set:',type(empty_set))
print('Datatype of set:',type(empty_dict))

#DUPLICATE
numbers = {2,3,6,8,10,2,4,3,5}
print(numbers)

#ADDING SET
nos = {21,22,90,89}
print('initial set:',nos)
nos.add(45)
print('updated set:',nos)

#UPDATED 
companies = {'TCS','IBM','DELL','TechM'}
Bpo = {'Southerland','qspider','Sitel'}
companies.update(Bpo)
print(companies)

#REMOVE
companies = {'TCS','IBM','DELL','TechM'}
print("Tech:",companies)
removecompanies = companies.discard('TechM')
print("Tech:",companies)

#ADD
prime_num = {2,5,2}
prime_num.add(11)
print(prime_num)

#CLEAR
prime_num = {2,5,2}
prime_num.clear()
print(prime_num)

#COPY: Copying from one set to another
nums = {1,2,3,4}
new_nos = nums.copy()
print(new_nos)

#DIFFERENCE
A = {1,3,5,7,9}
B = {2,3,5,7,11}
print(A.difference(B))
print(B.difference(A))

#UPDATED DIFFERENCE
A = {1,3,5,7,9}
B = {2,3,5,7,11}
A.differencce_update(B)
print('A=',A)

#DISCARD
nums ={2,3,5}
nums.discard(3)
print(nums)

#INTERSECTION JOIN()
A = {2,3,4}
B = {1,2,3}
print(A.intersection(B))

#INTERSECTION UPDATE()
A = {2,3,4}
B = {1,2,3}
A.intersection_update(B)
print('A=',A)

#DISJOINT()
A = {1,2,3,}
B = {4,5,6}
print(A.isdisjoint(B))

#ISSUBSET()
A = {1,2,3}
B = {1,2,3,4,5}
print(A.issubset(B))

#ISSUPERSET()
A = {1,2,3,4,5}
B = {1,2,3}
C = {1,2,3}
print(A.issuperset(B))
print(B.issuperset(A))
print(C.issuperset(C))

#POP-1
A = {'a','b','c','d'}
removed_item = A.pop()
print(removed_item)

#POP-2
A = {10,'TEN',100,'HUNDRED'}
print('POP:',A.pop())
print('New POP',A)

#REMOVE
techlang = {'c','c++','java','python'}
techlang.remove('c++')
print(techlang)

#SYMMETRIC DIFFERENCE
A = {'a','b','c','d'}
b = {'c','d','e'}
res = A.symmetric_difference(b)
print(res)

#SYMMETRIC DIFFERENCE UPDATE
A = {'a','c','d'}
b = {'c','d','e'}
res = A.symmetric_difference_update(b)
print(res)

#UNION()
A = {2,3,5}
B = {1,3,5}
print('a U b=',A.union(B))

#UPDATE
A = {'a','b'}
B = {1,2,3}
A.update(B)
print(A)

#TWO nSets
A = {1,3,5}
B = {3,5,1}
if A==b:
    print("Sets are equal")
else:
    print("Sets are not equal")
    
#SUM
marks = [65,90,68,0]
total_marks = sum(marks)
print(total_marks)

#SORT
marks = [65,90,68,0]
total_marks = sorted(marks)
print(total_marks)

#min 
marks = [65,90,68,0,-99,-8]
total_marks = min(marks)
print(total_marks)

#max 
marks = [65,90,68,0,-99,-8]
total_marks = max(marks)
print(total_marks)

#ENUMERATE
langs = ['python','c','c++']
enumerate_langs = enumerate(langs)
print(list(enumerate_langs))

#ANY
bool_list = ['True','False','True']
res = any(bool_list)
print(res)

#ALL
bool_list = ['True','False','True']
res = all(bool_list)
print(res)