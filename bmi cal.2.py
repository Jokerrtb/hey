height=float(input("enter your height in m "))
weight=float(input("rnter your weight in kg "))

solution=round(weight / height **2)

if solution < 18.5:
    print("you are underweight human ")
if solution <18 :
    print("you are a normal weight human ")
elif solution <25:
    print("you are a overweight human ")
elif solution <30:
    print("you are an obese human ")

else:
    print("you are cilincly obese ")






    

