Year= int(input("which year do want want to check? "))
#first step use the % 
if Year % 4 == 0:
    if Year % 100 == 0:
        if Year % 400 == 0:
            print(f"{Year} is a leap year ")
        else:
            print(f"{Year} is not a leap year ")
    else:
        print(f"{Year} is not a leap year ")
else:
    print(f"{Year} is not leap year ")





