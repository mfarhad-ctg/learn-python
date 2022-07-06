# Nasted Condition

age =int(input("What is Your Age? "))

if age >= 18:
    nationality = input("Do You have Your NID Card? (Y/N) ")
    if nationality =='Y':
        tradelicence= input("Do you have Trade Licence? (Y/N) ")
        if tradelicence =='Y':
            print("Congratulation!")

        else:
            print("You must have Trade Licence.")
    else:
        print("You Must have NID Card.")

else:
    print("You Must have 18+.")