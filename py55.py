#formatting

def print_formatted(number):
    padding=len(bin(number)[2:])
    for i in range(1,number+1):
        a=str(i)
        b=oct(i)[2:]
        c=hex(i)[2:]
        c=c.upper() # for uppercasing....without upercasing ex hex(10000):0x186a0 with uppercaising=0X186A0
        d=bin(i)[2:]
        print(a.rjust(padding," "),b.rjust(padding," "),c.rjust(padding," "),d.rjust(padding," "))

        #a.rjust(padding," ")-> prints whats given as 2nd parameter for 1st parameter times and after that
        #prints a
        #ex: a=2,padding=5          a.rjust(padding," ")-> prints    :     2(5 spaces and prints 2)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)