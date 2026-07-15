print("welcome to the tresureisland")
print("ur mission is to find the tresure")
choice1=input('you \'re in cross road where u want to move "left" or "right"')
if choice1=="left": #ur are getting error by "" use '' if we have again '' error use\
    #if we are getting long print statement we can split it into another line with correct indentation
    choice2=input('you moves towards the lake in the middle of the lake there is island then ' \
    'you \'ve to "wait" or "swim"\n')
    if choice2=="wait":
        choice3=input('there are 3 doors which door you want to ' \
    'wait "red"or "yellow" or "blue"\n')
        if choice3=="red":
            print("game over")
        elif choice3=="yellow":
            print("you are win")
        elif choice3=="blue":
            print("game over")
        else:
            print("you typed wrong colour")
    else:
        print("you are attacked by something game over bcoz u are swimmed")
else:
     print("game over due to you go to the hole thsat means u movew to right")


