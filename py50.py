a="anugrah"
b=set(a)
print(b) #every time to print a set...index of values change
b.add("xip")
print(b) #{'r', 'h', 'n', 'a', 'u', 'xip', 'g'}...not every time as it changes every time

#it even includes space as an element. b.add(" ")

# Input Format

# The first line contains an integer , the total number of country stamps.
# The next  lines contains the name of the country where the stamp is from.
# Constraints


# Output Format

# Output the total number of distinct country stamps on a single line.

a=int(input(""))
j=set()
for i in range(a):
    h=input()
    j.add(h)
k=len(j)
print(k)

#or

a=int(input(""))
j=set()
for i in range(a):
    h=input()
    j.add(h)
k=len(j)
print(k)



n = int(input())
s = set(map(int, input().split()))
d=int(input())
for _ in range(d):
    j=input().split()
    cmd=j[0]
    if len(j)==2:
        e=int(j[1])
    if cmd=="remove":
        s.remove(e)     #removes the element in it....error if not found
    elif cmd=="discard":
        s.discard(e)      #removes the element in it....no error if not found
    elif cmd=="pop":
        s.pop()      #last element removed if nothing given as parameter

sum1=sum(s)   #sum of elements
print(sum1)


a=int(input(""))
j=set(map(int, input().split()))
a2=int(input())
j1=set(map(int, input().split()))
un=j.union(j1) #joins the both sets removing duplicate elements
lenn=len(un) #length of set
print(lenn)