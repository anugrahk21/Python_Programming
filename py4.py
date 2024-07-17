x=67
def abc():
    x=10
    print(x)
def pqr():
    y=78
    print(x)
    print(y)
def xyz():
    global x
    x=50
    print(x)

abc()
pqr()
xyz()
print(x)
