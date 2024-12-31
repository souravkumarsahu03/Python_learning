n = int(input("Enter a number between 4 digit : "))
if(n<10):
    print(n,"is a 1 digit number.")
elif(n>=10 and n<100):
    print(n,"is a 2 digit number")
else:
    print(n, "is a 3 digit number")