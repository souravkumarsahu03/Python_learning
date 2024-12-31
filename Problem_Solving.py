# WAP to sort a dictionary by Value
student = {"name":"Sourav","rollNo":28,"dest":"android dev","id":430,"age":21}
ky = sorted(student.values())
print(ky)

# WAPython script to print a dict where the keys are numbers between 1 and 15 and the values are square key.
a = {}
for i in range(1,16):
    a[i] = i**2
print(a)

print("*"*40)

# WAP to multiply all the items in a dict.
item = {"rollNo":28,"r":8,"rg":12,"ro":2}
mul = 1
for i in item:
    mul *= item[i]
print(mul)

print("*"*40)

# WAP to sort a dict by key.
x = sorted(student.keys())
print(x)
print("*"*40)