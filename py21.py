x=int(input("table of"))
y=int(input("till"))
for i in range (1,y+1):
    if i>20:
        break
    else:
        print(x,"*",i,"=",x*i)
print("only till 20")
