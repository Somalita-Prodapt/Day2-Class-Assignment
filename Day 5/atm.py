balance=5000
amount=int(input("Enter the amount: "))
if amount <=balance and amount %100==0:
    balance-=amount
    print("Withdrawal successful")
    print("Remaining Balance:", balance)
else:
    print("Invalid withdrawal")
