#any(iterable) yields True if at least one element within the iterable is evaluated as true and False otherwise
if __name__ == '__main__':
    s = input()
    if (any(i.isalnum() for i in s))==True: #if any of i(element) is true
        print("True")
    else:
        print("False")
    if (any(i.isalpha() for i in s))==True:
        print("True")
    else:
        print("False")
    if (any(i.isdigit() for i in s))==True:
        print("True")
    else:
        print("False")
    if (any(i.islower() for i in s))==True:
        print("True")
    else:
        print("False")
    if (any(i.islower() for i in s))==True:
        print("True")
    else:
        print("False")
