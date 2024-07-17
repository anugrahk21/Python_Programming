a=10#1st
a1="hello"
a2=10.123
a3=100000000
a4=True
print(type(a))
print(type(a1))
print(type(a2))
print(type(a3))
print(type(a4))


x=y=z=456#2nd
print(x)


x,y=y,x#3rd


x,y,z=123,1,"hello"#4th
print(x)
print(y)
print(z)


a=int(input("enter 1st no"))#5th
b=int(input("enter 2nd no"))
a=a+b
b=a-b
a=a-b
print(a)
print(b)
