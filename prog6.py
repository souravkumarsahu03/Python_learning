# WAP to find sum of odd numbers between 10 using while loop 

n=0
sum = 0
while n<=20:
    if n % 2 != 0:
        sum = sum+n
    n = n+1
print(f"sum of all first 10 odd numbers are : {sum}")