
student = {"name":"Sourav","rollNo":115,"id":430,"age":21}
print(student["age"])
print(student["name"])
print(student["id"])


# Iteration in DICT 

# Printing all the keys name in the dict 
for i in student:
    print(i)

# Printing all the values name in the dict 

for x in student:
    print(student[x])

print("*"*40)


    # using value function 
for y in student.values():
    print(y)
print("*"*40)


# using items function 

for x,y in student.items():
    print(x,"=",y)