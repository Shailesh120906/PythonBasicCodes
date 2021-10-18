import random

def gamewin(cturn ,pturn):
    if cturn == pturn:
            return None
    elif cturn == "s":
        if pturn == "w":
            return False
        if pturn == "g":
            return True
    elif cturn == "w":
        if pturn == "s":
            return True
        if pturn == "g":
            return False
    elif cturn == "g":
        if pturn == "w":
            return True
        if pturn == "s":
            return False
    else:
        print("Please enter s, w or g. Nothing Else :)")


print("Computer's Turn Recorded")
compchoice = random.randint(1 ,3)
if compchoice == 1:
    cturn = "s"
elif compchoice == 2:
    cturn = "w"
elif compchoice == 3:
    cturn = "g"

pturn = input("Enter Your Move : (S)nake ,(W)ater ,(G)un : ")
if gamewin(cturn,pturn):
    print("You Won !!!")
else:
    print("You Lost :(")
print("Computer's Choice was",cturn)
