#sorting bases on kth element of the list of subset
if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    #key specifies on what basis we need to sort
    arr.sort(key=lambda x: x[k]) #lambda x: x[k] is an anonymous function (lambda function) that 
                         #takes one argument x (which will be a sublist) and returns the k-th element of that sublist.
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j],end=" ")
        print()
    # or 
    for i in arr:
        print(*i)   #removes the list brackets