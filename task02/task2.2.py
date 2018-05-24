"""
Write a program to calculate total cost.
One item costs M dollars and N cents. Customer bought L items.
Print total price in dollars and cents for L items.
"""
amdol = (input("Enter the amount in $ "))

amcent = (input("Enter the amount in cents "))

amount = float(amdol + "." + amcent)

quantity = int(input("Enter the quantity in $ "))

total = amount * quantity

print("Total is ", total, "$")




