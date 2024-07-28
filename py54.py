#String Split and Join

def split_and_join(line):
    a=line.split()
    b="-".join(a)    #this-is-a-string
    return b

if __name__ == '__main__':
    line = input()        #input=this is a string
    result = split_and_join(line)
    print(result)