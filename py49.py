#list comprehension
x=[[i,i] for i in range(5)]#nested list
print(x) #[[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]

y=[i for i in range (5)]
print(y) #[0, 1, 2, 3, 4]

z=[[i,j] for i in range(5) for j in range(3)]#nested list
print(z)  #[[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0],
#           [2, 1], [2, 2], [3, 0], [3, 1], [3, 2], [4, 0], [4, 1], [4, 2]]


n=5
u,v,w=1,2,3
l=[[p,q,r] for p in range(u+1) for q in range(v+1) for r in range(w+1) if (p+q+r)!=n] #giving condition
print(l) #[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 0, 3], [0, 1, 0],
#             [0, 1, 1], [0, 1, 2], [0, 1, 3], [0, 2, 0], [0, 2, 1], [0, 2, 2],
#             [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 0, 3], [1, 1, 0], [1, 1, 1],
#             [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 3]]