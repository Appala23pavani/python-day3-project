#modulo %
#it gives remainder as a result
#let us take an example
#10%3 is 1 #the reaminder is 1
#any even num is divided by 2 is 0
#ex: 12%2==0
# if divide odd num with the 2 it gives remainder as 0
#question:
# what is 10%3 and also check it is even or odd
print(10%3)
n=int(input("enter a number"))
if n%2==0:
    print("even")
else:
    print("odd")