a = ("Onplus","Nokia","Redmi")
print("before conversion", type(a))

a = list(a)
print("after conversion", type(a))


a.append("Vivo")
print(a)

# converting agoin it into tuple
a = tuple(a)
print(type(a))