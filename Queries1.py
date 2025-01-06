#SAMSKRUTI SHOP PRGM
print("SAMSKRUTI SHOP BILL")
Section1 = 10000
Section2 = 20000
Section3 = 20000
total_bill = Section1+Section2+Section3
discount = 10/100 * total_bill
total_amount = total_bill - discount
print("Total Bill:₹",total_bill)
print("Discount(10%):₹",discount)
print("Total amount:₹",total_amount) 

#SAMSKRUTI RESTAURANT PRGM
print("SAMSKRUTI RESTAURANT BILL")
starters = 150 
main_course = 300
dessert = 300
sub_total = starters+main_course+dessert
gst_amount = 18/100 * sub_total
total_amount = sub_total + gst_amount
print("Sub Total:₹",sub_total)
print("GST(18%):₹",gst_amount)
print("Total amount:₹",total_amount)

#DYNAMIC OTP GUESSING GAME
import random
otp = str(random.randint(10000, 99999))  
print("Guess the OTP!")
guess = input("Enter your guess: ")
if guess == otp:
    print("Correct! You guessed the OTP.")
else:
    print(f"Wrong! The OTP was: {otp}")

#COUNT AND COMPARE '*' AND '#' IN STRING
S = input("Enter the string consisting of '*' and '#': ")
count_star = S.count("*")
count_hash = S.count("#")
if count_star>count_hash:
    print("Positive number")
elif count_hash>count_star:
    print("Negative number")
elif count_hash == count_star:
    print("0")
    
#COLOR COLOR WHICH COLOR? - A FUN COLOR MATCHING GAME
print("Welcome to 'Color Color Which Color?' game!")
print("Rules: Enter a color and see the result. Have fun!\n")
color = input("Color Color Which Color?: ").strip().lower()
if color == "blue":
    print("Boy")
elif color == "pink":
    print("Girl")
elif color == "white":
    print("None")
else:
    color=="black"
    print("ERROR")

#You receive a fixed amount of pocket money each week and want to know how much you will have after saving for a
#certain number of weeks. Create a Python program that takes the amount of pocket money per week and the number
#of weeks as input and calculates the total amount saved.

weekly_amount = float(input("Enter the weekly pocket money amount: "))
number_of_weeks = int(input("Enter the number of weeks: "))
total_saved = weekly_amount * number_of_weeks
print(f"Total amount saved after {number_of_weeks} weeks is: {total_saved}")

#You have a certain number of candies and chocolates to distribute equally among your friends.
#Write a Python program that takes the total number of candies and the number of friends as input and 
#calculate how many candies or chocolates each friend will get and how many will be left over.
#Total candies: 12
#Number of friends: 4

total_candies = int(input("Enter the total number of candies: "))
number_of_friends = int(input("Enter the number of friends: "))
candies_per_friend = total_candies // number_of_friends
leftover_candies = total_candies % number_of_friends
print(f"Each friend gets {candies_per_friend} candies.")
print(f"{leftover_candies} candies are left over.")

#You are planning a movie marathon and want to know how many full movies you can watch in a day. 
#Write a Python program that takes the duration of a single movie and 
#the total time you have for watching movies as input, and calculate 
#how many full movies you can watch and how much time will be left.
#Input: Movie duration = 120 minutes
#Total time available = 500 minutes

movie_duration = int(input("Enter the duration of a single movie (in minutes): "))
total_time = int(input("Enter the total time available (in minutes): "))
full_movies = total_time // movie_duration
leftover_time = total_time % movie_duration
print(f"You can watch {full_movies} full movies.")
print(f"Time left after watching movies: {leftover_time} minutes.")

