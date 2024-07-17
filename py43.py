import random
b=random.randint(1,101)
while True:
    c=int(input("enter your guess: "))
    if b==c:
        print("guessed right and its:",b)
    elif b!=c:
        if b-c<3:
            print("wrong!,almost there!")
        elif c-b>20:
            print("wrong!, more to go!")
        elif b-c<20:
            print("just a little")
        elif c-b<20:
            print("just a liile")