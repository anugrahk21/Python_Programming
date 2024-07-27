a=int(input())
aa=list(map(int, input().split()))
g=len(aa)
p=g//a
d={}
for i in aa:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in (d.keys()): #keys of dictionary
    j=d.get(i)   #values of that key
    if j!=a:
        print(i)
        break
        
#we did this program in dictionary because dictionary uses less time than list,set



#using list,set
a=int(input())
aa=list(map(int,input().split()))
g=len(aa)
p=g//a
s=set(aa)
for i in s:
    k=aa.count(i)   #this takes many time
    if k!=a:
        print(i)
