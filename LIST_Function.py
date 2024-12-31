a= ["hanuman","superman","batman","ironman","batman"]
print(a)

# for finding length of the list 
print(len(a))

# to count an occurence of a particular element
print(a.count("batman"))

# to add new element
a.append("hulk")
print(a)

# to add to a specific location
# INSERT METHOD
a.insert(2,"deadpool")
print(a)

# to remove from a list
a.remove("hulk")
print(a)

# to remove from a certain location
a.pop(2)
print(a)


# to create a copy of a list
b = a.copy()
print(b)

# to access an element
print(a.index("batman"))


# to extend the list
c = ["vison","spidermon"]
a.extend(c)
print(a)


# to reverse the list
a.reverse()
print(a)


# to sort the list 
a.sort()
print(a)
d = [1,7,8,4,9]
d.sort()
print(d)

# to clear all the data from the list 
d.clear()
print(d)