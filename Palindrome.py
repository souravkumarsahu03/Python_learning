num = int(input("Enter a number : "))
rev = 0
temp = num
while(num > 0):
    dig = num % 10 
    rev = rev*10 + dig
    num = num//10

if rev == temp:
    print("Palindrome")
else:
    print("Not a palindrome")