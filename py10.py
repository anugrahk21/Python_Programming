for i in range(1,51):
    if i%3==0 and i%5==0:
        print("fizz bus")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("bus")
    elif i%3==0 and i%5==0:
        print("fizz bus")
    else:
        print(i)
