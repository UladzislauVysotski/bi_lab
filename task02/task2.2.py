"""
Write a program to calculate total cost.
One item costs M dollars and N cents. Customer bought L items. Print total price in dollars and cents for L items.
"""
amount = float(input("Enter the amount in $ "))

quantity = int(input("Enter the quantity in $ "))

remainingamount = float(amount * quantity)

print("Total is ", remainingamount, "$")
