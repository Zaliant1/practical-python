from sympy import Sum


expenses = [10.50, 8, 5, 15, 20, 5, 3]
total = 0


for i in expenses:
    total += i

print(f"You spend ${total}")


total2 = 0
expenses2 = []
for i in range(8):
    expenses.append(float(input("Enter an expense:")))

total2 = sum(expenses2)

print(f"You spend ${total2}")
