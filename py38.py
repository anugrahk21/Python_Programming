class k23hp:
    def __init__(self,roll_no,name):
        self.roll_no=roll_no
        self.name=name
roll_no=input("roll: ")
name=input("name: ")
abc=k23hp(roll_no,name)
print(abc.name)
print(abc.roll_no)


class ett:
    def stress(self,code,moti=None,exp=None):
        if code=="INT108" and exp==None:
            print("re")
        elif code=="INT108" and exp==40:
            print("pass")
el=ett
el.stress("INT108")
el.stress("INT108",None,40)