# WAP to find max and min in a set 
a = {12,35,67,43,24,53}
maxi = max(a)
mini = min(a)
print("Max val is :",maxi)
print("Min val is :", mini)
print("*"*60)

# WAP to find common elements in three lists using sets
x = [1,5,6,4,5]
y = [4,5,6,7]
z = [1,9,3,2,5,6,1,3]

print("Common elements are >>> ",set(x) & set(y) & set(z))

print("*"*60)

# WAP to find difference between two sets
x1 = {1,5,6,4,5}
y1 = {4,5,6,7}

print(x1.difference(y1))
print("*"*60)



# WAP to remove an item from a set if it is present in the set
s = {1,5,6,4,5}
s.discard(1)
print(s)

print("*"*60)


# WAP to check if a set is a subset of another set
l = {1,5,6,4,5}
m = {2,3,4}

print(l.issubset(m))
