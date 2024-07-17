str1="THIS IS K23HP CLASS"
print(str1[6])
print(str1[-6])
print("VM" in str1)
c=0
for i in str1:
    if i in ["A","E","I","O","U"]:
        c+=1
        
print("total no of vovels",c)

