S = input("Enter the string consisting of '*' and '#': ")
count_star = S.count("*")
count_hash = S.count("#")
if count_star>count_hash:
    print("Positive number")
elif count_hash>count_star:
    print("Negative number")
elif count_hash == count_star:
    print("0")
        
    