'''n=int(input("enter num"))
n1=0
n2=1
if n==0:
    print("enter +ve integer")
else:
    while >0:
        n3=n1+n2
        n2=n1
        n2=n3
        n-=1
    print(n3)'''

nterms = int(input("How many terms? "))
num1, num2 = 0, 1
count = 0
series = []

if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    series.append(num1)
else:
    while count < nterms:
        series.append(num1)
        nth = num1 + num2
        num1 = num2
        num2 = nth
        count += 1

print("Fibonacci sequence:")
for i in series:
    print(i)

'''else:
    for i in range(0,n+1):
        n1=i+n2
        n2=i
        i=n1
        n-=1
        print(n1)'''
