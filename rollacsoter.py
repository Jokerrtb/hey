print("welcome to the rollarcoster ")
height= int(input("what is your height in cm pls? "))

if height >= 120:
    print("you can ride the rollarcoaster! ")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print('A child ticket cost $5. ')
    elif age <= 18: 
        bill = 7
        print("Yoth tickets are $7. ")
    else:
        bill = 12
        print('Adult tickets are $12. ')
    
    want_photo = input("Do you want a photo? Y or N. ")
    if want_photo == "Y":
        bill  += 3

else:
    print("sorry pele you are tall enough to ride this now ")





