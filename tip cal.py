print("welcome to my tip calulator ")
bill=   float(input("what was your total bill?  $"))
people1= int(input("how many people want to spilt the bill? "))
tip=   int(input('what per of tip do you want to take 10,12,15? '))

tip1=tip/100
tip2=bill * tip1
tip3=tip2 + tip2

tip4=tip3/people1
tip5=round(tip4)
print(f"each people will have to pay: ${tip5} ") 








