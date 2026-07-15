# syntax
#if condition1:
#do A
#elif condition2:
#do b
#else:#above conditions are not true then we use this
#do c
print("welcome to the roaster")
height=int(input("what is ur height in cm"))
if height>120:
    print("can ride")
    age=int(input("enter ur age"))
    if age<=12:
        print("pay $5")
    elif age<=18:
        print("pay $7")
    else:
        print(" pay 12$")

else:
    print("can't ride")
    #only true statement is executed
