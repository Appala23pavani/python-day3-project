#question is:
#welcome to tje python pizza delivery:
#size of the pizza s or m or l:
#add peppor yes or no?
#add extra cheese or not?
#small pizza(s):5
#medium pizza(m):$7
#large pizza(l):$10
#if we want to add peppor to small pizza add $2
#if we want to add peppor to m or l pizza ass $3
#if we want  to add extra cheese to any pizza add $1
#/// no solve the prblm with pytho code
print("welcome to the python pizza delivery")
size=input("size of the pizza S or M or L?")
add_peppor=input("add peppor to the pizza yes or no?")
extra_cheese=input("add extra cheese to the pizza yes pr no?")
bill =0
if size == "s":
    bill+=5
elif size == "m":
    bill+=7
elif size == "L":
    bill+=10
else:
    print("u typed a wron type of pizza")
if add_peppor == "yes":
    if size=="s":
        bill+=2
    else:
        bill+=3
if extra_cheese=="yes":
    bill+=1

print(f"final bill is: ${bill}.")
