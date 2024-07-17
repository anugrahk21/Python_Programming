class perfectno:
    def perfect(self,a):
        c=0
        for i in range(1,a):
            if a%i==0:
                c+=i
        if c==a:
            print("perfect no")
        else:
            print("non p no")
b=int(input("enter:"))
pno=perfectno()
pno.perfect(b)