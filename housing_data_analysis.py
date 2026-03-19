import pandas as pd
import matplotlib.pyplot as plt

# Sample housing data
data = {
    "Location": ["Dublin", "Dublin", "Cork", "Galway", "Dublin", "Cork", "Limerick"],
    "Price": [1200, 1500, 900, 800, 1300, 950, 700],
    "Website": ["A", "B", "A", "A", "C", "B", "A"],
    "Available": ["Yes", "No", "Yes", "Yes", "Yes", "No", "Yes"]
}

df = pd.DataFrame(data)

print("Original Data")
print(df)

# count houses per location
location_count = df["Location"].value_counts()

print("\nHouses per location")
print(location_count)

# average price per location
avg_price = df.groupby("Location")["Price"].mean()

print("\nAverage price per location")
print(avg_price)

# count listings per website
website_count = df["Website"].value_counts()

print("\nListings per website")
print(website_count)

# filter available houses
available_houses = df[df["Available"] == "Yes"]

print("\nAvailable houses")
print(available_houses)

# plot graph
location_count.plot(kind="bar")

plt.title("Number of Houses per Location")
plt.xlabel("Location")
plt.ylabel("Count")

plt.show()
