A = ["Ross","Rachel","Tony","Jhonny"]


# WAP to swap first and last element 
A[0], A[3] = A[3], A[0]
print(A)

# WAP to add a new value at sec postion 
A.insert(1,"Stark")
print(A)

# WAP to delete a value from 3rd position 
A.pop(2)
print(A)


B = [13,7, 12, 10]

# WAP to multiply all the numbers in the list 
mul = 1
for i in (B):
    mul *= i
print(mul)

# WAP to get the largest number from the list 
B.sort()
print("the largest value in the list is :", B[-1])

# WAP to get the smallest number from the list 
print("the smallest value in the list is :", B[0])