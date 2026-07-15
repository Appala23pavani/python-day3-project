#nested if or else
# it means inside the if statement it contains another if
                #flow chart
                 #condition
#no                                  #yes
                                    #condition
                               #no             #yes
#let us take roller roaster example
print("welcome to the roaster")
height=int(input("what is ur height in cm"))
if height>120:#this condition is true then only u can go to another if condition
    print("can ride")
    age=int(input("enter ur age"))
    if age>20:#nested if
        print("pay 40$")
    else:
        print("pay 20$")#upto here nested if
else:
    print("can't ride")

