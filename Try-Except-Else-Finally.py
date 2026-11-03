
balance = 5000

try:
    print("Current Balance:", balance)

    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise ValueError("Amount must be greater than zero!")

    if amount > balance:
        raise Exception("Insufficient balance!")

    balance = balance - amount

except ValueError as e:
    print("Invalid Input:", e)

except Exception as e:
    print("Transaction Failed:", e)

else:
    print("Transaction Successful!")
    print("Withdrawn Amount:", amount)
    print("Remaining Balance:", balance)

finally:
    print("Transaction process completed.")
    print("Thank you for using our banking system!")
