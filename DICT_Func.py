student = {"name":"Sourav","rollNo":28,"id":430,"age":21}


# get
x = student.get("age")
print(x)
print("*"*40)


# item
y = student.items()
print(y)
print("*"*40)


# keys
ky = student.keys()
print(ky)
print("*"*40)


# values
v = student.values()
print(v)
print("*"*40)


# copy
cpy = student.copy()
print(cpy)
print("*"*40)


# set default
deeef = student.setdefault("rollNo",24)
print(deeef)
print("*"*40)
# update


print("*"*40)
# pop 


print("*"*40)

# popitem



print("*"*40)
# clear



print("*"*40)