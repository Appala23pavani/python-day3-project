print("welcome to the roaster")
height=int(input("what is ur height in cm"))
if height>120:
    print("can ride")
    age=int(input("enter ur age"))
    if age<=12:
        print("pay $5")
    elif age<=18:
        print("pay $7")
    elif age>35 and age<45:      #age is between 35-45
        print("pay $40")
    else:
        print(" pay 12$")

else:
    print("can't ride")