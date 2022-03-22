def openRussianDoll(doll):
    if doll == 1:
        print("All dolls are opened")
    else:
        print("Opened doll no. {}".format(doll))
        openRussianDoll(doll-1)

openRussianDoll(4)