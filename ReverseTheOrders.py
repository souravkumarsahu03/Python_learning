s = input("Enter some string : ")
l = s.split()
l1 = []
i = len(l) - 1
# print(i)
while i>=0 :
    l1.append(l[i])
    i -= 1
op = ' '.join(l1)
print(op)