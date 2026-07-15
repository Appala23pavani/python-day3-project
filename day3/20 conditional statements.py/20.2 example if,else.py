#let take an example age=20 print yes when age is greater than 18 other wise print no
age=20
if age>18:
    print("yes")
else:
    print("no")

#example 2
#welcome to the roaster ride if height is greater than 120cm print can ride
#otherwise print can't ride
print("welcome to the roaster")
height=int(input("what is ur height in cm"))
if height>120:
    print("can ride")
else:
    print("can't ride")
#another example:
print("welcome to the roaster")
height=int(input("what is ur height in cm"))
if height>=120:
    print("can ride")
else:
    print("can't ride")

#these are the comparision operators
#> # greater than
#<# less than
#>=  #greater than or equal to
#<= #less than or equal to
#== #equal to
#=! #not equal to


#some time we use single = that means assiging value to the variable
#==  it means equality of lef and right values
height=int(input("what is ur height in cm"))
if height==120:
    print("can ride")
else:
    print("can't ride")
#using not equal to:
height=int(input("what is ur height in cm"))
if height!=120:
    print("can ride")
else:
    print("can't ride")

