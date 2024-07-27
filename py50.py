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
inter=j.intersection(j1) #elements which are in both sets(common elements)
diff=j.difference(j1)  #difference(j-j1)...elements of j1 which are not present in j.(uncommon elements)
symmdiff=j.symmetric_difference(j1) #uncommon elements in both the sets...elements which are not in common in both the sets.
print(symmdiff)
print(diff)
lenn=len(un) #length of set
print(lenn)
print(inter)


n=int(input(""))
s=set(map(int,input().split()))
no=int(input())
for i in range(no):
    op=list(map(str,input().split()))
    n1=int(op[1])
    cm=op[0]
    s2=set(map(int,input().split()))
    if cm=="intersection_update":
        s.intersection_update(s2)    #updates the set with intersection set of both set
    elif cm=="update":
        s.update(s2)      #updates the set with the given elements at the last positions
    elif cm=="difference_update":
        s.difference_update(s2)       #updates the set with the difference set of both set
    elif cm=="symmetric_difference_update":
        s.symmetric_difference_update(s2)     #updates the set with the uncommon elements of both the set
ss=sum(s)   #sum of the set elements
print(ss)


#subset

a=int(input())
for i in range(a):    #number of tes cases
    sl1=int(input())
    s1=set(map(str,input().split()))
    sl2=int(input())
    s2=set(map(str,input().split()))
    k=True
    for i in s1:
        if i in s2:
            k=True
        else:
            k=False
            break
    print(k)


#superset

sm = set(map(str, input().split()))
a = int(input())
k = True

for _ in range(a):
    s1 = set(map(str, input().split()))
    # Check if sm is a proper superset of s1
    if not (sm.issuperset(s1) and sm != s1): #sm should not be equal to s1
        k = False
        break

print(k)

#long method
sm=set(map(str,input().split()))
a=int(input())
k=True
for i in range(a):
    s1=set(map(str,input().split()))
    if k==False:
        break
    for i in s1:
        if i in sm:
            k=True
        elif i not in sm:
            k=False
            break
    if sm==s1:
        k=False
        break

print(k)

