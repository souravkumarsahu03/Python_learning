a = {"Ironman","superman","hulk","spidorrrmonnn"}


# add
a.add("captainAmerica")
print(a)


# pop 
a.pop()
print(a)


# remove 
a.remove("hulk")
print(a)


# discard
a.discard("ironman")
print(a)


# copy 
b = a.copy()
print(a,"=",b)



an= {"hulk","ironman","thor","vision"}
a2= {"superman","batman","spidermonnn"}
a3= {"hulk","thor"}


# is disjoint 
print(an.isdisjoint(a3)) 

# is subset >> is a sub set of other or not 
print(an.issubset(a2))

# is superset
print(an.issuperset(a3))

# update
x = an.update(a3)
print(x)


# clear
# a1.clear()
# print(a1)

# UNION 
un = an.union(a2)
print(un)

# DIFFERENCE
dif = an.difference(a2)
print(dif)