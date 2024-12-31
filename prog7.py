# WAP to check if a number is divisble by 8 and 12, up to 100 numbers

# n = int(input("Give one +ve number between 1-100 : "))
for i in range(1, 101):
    if i % 8 == 0 and i % 12 == 0:
        print(i)
