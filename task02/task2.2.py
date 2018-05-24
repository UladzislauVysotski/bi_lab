"""
Write a program to calculate total cost.
One item costs M dollars and N cents. Customer bought L items.
Print total price in dollars and cents for L items.
"""
amount: float = float(input("Enter the amount in $ "))

quantity = int(input("Enter the quantity in $ "))

total = amount * quantity

print("Total is ", total, "$")
