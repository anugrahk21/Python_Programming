#mapping and eval function
x, k = list(map(int, input().split()))# Read input, split by whitespace, convert each to int, and create a list...here  x=1(as per sample) k=4
print(x)
print(k)
P = input()
print(eval(P) == k)# here in eval (takes string as expression).. it evaluates the function by take the value of x in it.
a,b=[1,2]
print(a,b)#a=1,b=2

a=input()
j=exec(a) #or eval(a)
if j is not None: #as we can give a print statement for eval oe exec it should only print if the value is not none....otherwise after the result a "none" is printed
    print(j)

