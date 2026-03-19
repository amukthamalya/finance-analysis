import pandas as pd
import matplotlib.pyplot as plt

# Sample finance data
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Income": [2000, 2200, 2100, 2500, 2400, 2600],
    "Expense": [1500, 1600, 1400, 1700, 1800, 1750]
}

df = pd.DataFrame(data)

# Calculate profit
df["Profit"] = df["Income"] - df["Expense"]

print("Finance Data")
print(df)

# Total values
total_income = df["Income"].sum()
total_expense = df["Expense"].sum()
total_profit = df["Profit"].sum()

print("\nTotal Income:", total_income)
print("Total Expense:", total_expense)
print("Total Profit:", total_profit)

# Average profit
avg_profit = df["Profit"].mean()
print("Average Profit:", avg_profit)

# Plot graph
plt.figure(figsize=(8,5))

plt.plot(df["Month"], df["Income"], label="Income")
plt.plot(df["Month"], df["Expense"], label="Expense")
plt.plot(df["Month"], df["Profit"], label="Profit")

plt.title("Finance Analysis")
plt.xlabel("Month")
plt.ylabel("Amount")

plt.legend()

plt.show()
