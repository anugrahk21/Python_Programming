#mapping and eval function
'''
x, k = list(map(int, input().split()))# Read input, split by whitespace, convert each to int, and create a list...here  x=1 k=4 if input=1 4
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
'''
q,w=map(int,[1,2]) #q,w=map(int,[1,2,3])->error..not enough variables
print(q)#1
print(w)#2

e,r=[1,2]#e,r=[1,2,3]->error..not enough variables
print(e,r) #1 2

e1,*r1=[1,2,3]#e,*r=[1,2,3]-> not an error..here all the other values other than e1(1) will go to r1 as a list
print(e1,r1) #1 [2,3]
print(r1[0]) #first index value of r1.....2.