# WAP to find summ of all odd numbers between 1 to 50 
sum = 0
for i in range(0,51):
    if(i%2!=0):
        sum += i
print(sum)