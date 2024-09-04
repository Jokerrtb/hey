#display
print("welcome to my tip calcultor")
total_bill=float(input("what is your total bill? $"))
money_spilted=int(input("how many people want to split the bill? "))
tip=int(input("what percentage do you want to give? 10, 12 or 15 "))

#codes
tip_per = tip/100
total_tip= tip_per * total_bill
total_bill_tip= total_bill + total_tip

total_bill_perperson= total_bill_tip / money_spilted
final_amount= round(total_bill_perperson,2)

print(f"each person should pay {final_amount} dollar")
