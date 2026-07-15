#syntax
#if condition1:
# do A
#if condition2:
#do B
#if condition3:
#do C
#All conditions are true then all are executed
print("welcome to the roaster")
height=int(input("what is ur height in cm"))
if height>120:
    print("can ride")
    age=int(input("enter ur age"))
    if age<=12:
        bill=5
        print("ur are child pay $5")
    elif age<=18:
        bill=7
        print(" ur are youth pay $7")
    else:
        bill=12
        print(" u are adult pay 12$")
    you_want_photo=input("you want photo yes or no")
    if you_want_photo == "yes":#"if you are giving string add ""
        bill += 3
    print(f"final_bill${bill}")

else:
    print("can't ride")