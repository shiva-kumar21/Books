#Reverse  a number/Palindrome number-1
a = 123
a = int(str(a)[::-1])
print(a)
    
# A shop named Samskruti has 3 sections of items with 10% discount, total bill is 50000. Find the total amount spent.
total_bill = 50000
discount = total_bill*0.10
total_amount = total_bill - discount
print("Total bill amount: \u20B9", total_bill)
print("Discount(%10): \u20B9", discount)
print("total amount after discount: \u20B9",total_amount)

#Print the sum of 1st 10 multiples of a given number.
number = int(input("Enter a number"))
sum =sum(number * i for i in range(1,11))
print(f"Sum of multiples of {number} is {sum}")

#Find the highest number in given list.
l=[1,2,5,-4]
for i in l:
    print(i)
highest_number=max(l)
print("Highest number:",highest_number)

#2nd method
numbers = [10, 23, 45, 67, 89, 21, 56]
highest_number = numbers[0]
for number in numbers[1:]:
    if number > highest_number:
        highest_number = number
print("The highest number is:", highest_number)

#3rd method - Find highest number
numbers = [10, 23, 45, 67, 89, 21, 56]
numbers.sort()
highest_number=numbers[0]
for i in range(len(numbers)):
    if(highest_number<numbers[i]):
        highest_number=numbers[i]
print("The highest number is:",highest_number)

# Find the second highest number method-1
numbers = [10, 23, 45, 67, 89, 21, 56]
highest_number = max(numbers)
numbers.remove(highest_number)
second_highest_number = max(numbers)
print("The highest number is:", highest_number)
print("The second highest number is:", second_highest_number)

#Method-2
numbers = [10, 23, 45, 67, 89, 21, 56]
highest_number = numbers[0]
second_highest_number = numbers[0]
for num in numbers:
    if num > highest_number:
        second_highest_number = highest_number
        highest_number = num
    else:
        num > second_highest_number and num != highest_number
        second_highest_number = num
print("The highest number is:", highest_number)
print("The second highest number is:", second_highest_number)

#Swap the number using temporary variable
a = 5
b = 10
print("Before swapping:")
print("a =", a)
print("b =", b)
temp = a
a = b
b = temp
print("After swapping:")
print("a =", a)
print("b =", b)

#Find if the given input is a leap year or not?
year=int(input("Enter a year:"))
if (year % 4) == 0 and  (year % 100) != 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year")
    
#PATTERN PRINTING
#TRIANGLE
print("TRIANGLE")
rows=5
for i in range(1,rows+1):
    print('*'*i)

#PYRAMID 
print("PYRAMID")   
n = 5
for i in range(n):
    print(' '*(n-i-1)+'*'*(2*i+1))
     
#PRINT NO. OF YEARS, WEEKS, DAYS FROM GIVEN INPUT
n = int(input("Enter a input:"))
years = n//365
weeks= (n%365)//7
days = (n%365)%7
print(f"{n} days is equal to {years} years, {weeks} weeks, and {days} days.")

#ELECTRICITY BILL
'''In this problem you need to write a program calculate the electricity bill for a household, based on th eunits of elctricity the household consumed.
The price for unit varies based on the slab. The charges per unit for different slabs are as mentioned
For the first 50 units (0-50), the charge is 2/unit. For the next 100 units (51-150), 
the charge is 3/unit for the next 100 units (151-250), the charge is 5/unit. 
For above 250 units (251 and above), the charge is 8/unit.'''
'''Apart from these charges, there in also an additional s of 20% on the total amount is added to the bill'''
units = int(input("Enter the number of units consumed: "))
total_amount = 0
if units <= 50:
    total_amount = units * 2
elif units <= 150:
    total_amount = 100 + (units - 50) * 3
elif units <= 250:
    total_amount = 100 + 300 + (units - 100) * 5
else:
    total_amount = 100 + 300 + 500 + (units - 250) * 8
surcharge = total_amount * 0.2
total_amount += surcharge
print(f"The total electricity bill is: Rs {total_amount}")

             




    

