class fibonicci:
    def fibonicci_1(self,a):
        u=0
        v=1
        print(u)
        for i in range(1,a):
            c=u+i
            print(c)
            u=v
            v=c
z=int(input("enter:"))       
f1=fibonicci()
f1.fibonicci_1(z)


