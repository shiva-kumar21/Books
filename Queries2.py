#money:
def pocket_money_cal(no_of_weeks):
    total_pocket_money = 0
    for i in range(1,no_of_weeks+1):
        user_weekly_pocket_money = int(input(f"Enter {i} week pocket money"))
        total_pocket_money += user_weekly_pocket_money
        return total_pocket_money
no_of_weeks = int(input("Enter the no.of weeks to calculate the pocket money:-"))
calculated_pocket_money = pocket_money_cal(no_of_weeks)
print(f"Total pocket money of{no_of_weeks} weeks is Rupees {calculated_pocket_money}/-")
 







