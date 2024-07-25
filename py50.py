a="anugrah"
b=set(a)
print(b) #every time to print a set...index of values change
b.add("xip")
print(b) #{'r', 'h', 'n', 'a', 'u', 'xip', 'g'}...not every time as it changes every time

#it even includes space as an element. b.add(" ")

# Input Format

# The first line contains an integer , the total number of country stamps.
# The next  lines contains the name of the country where the stamp is from.
# Constraints


# Output Format

# Output the total number of distinct country stamps on a single line.

a=int(input(""))
j=set()
for i in range(a):
    h=input()
    j.add(h)
k=len(j)
print(k)

#or

a=int(input(""))
j=set()
for i in range(a):
    h=input()
    j.add(h)
k=len(j)
print(k)