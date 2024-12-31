while True:
    name = input("Enter the customer's name : ")
    total  = 0
    while True:
        print("Enter the amount and quantity")
        amount = float(input("Enter the amount : "))
        quantity = int(input("Enter the quantity : "))
        total += amount * quantity
        repeat = input("Do you want to add more items? (YES/NO) : ")
        if repeat == "NO" or repeat =="no":
            break
    print("-"*50)
    print("Name: ", name)
    print("Amount to be paid: ", total)
    print("-"*50)
    print("*********HAPPY SHOPPING**********")

    repeat1 = input("do you want to go to next customer? (YES/NO): ")
    if repeat1 == "no" or repeat1 == "no":
        break