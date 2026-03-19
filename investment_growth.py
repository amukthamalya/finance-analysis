initial = 1000
rate = 5
years = 5

amount = initial

for i in range(years):
    amount = amount + (amount * rate / 100)

print("Final amount:", amount)
