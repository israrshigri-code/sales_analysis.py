import pandas as pd
import matplotlib.pyplot as plt

# Sample Sales Data
data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Laptop", "Mobile"],
    "Sales": [50000, 30000, 20000, 60000, 35000]
}

df = pd.DataFrame(data)

# Total Sales
total_sales = df["Sales"].sum()

# Sales by Product
sales_by_product = df.groupby("Product")["Sales"].sum()

print("Total Sales:", total_sales)
print("\nSales by Product:\n", sales_by_product)

# Plot Graph
sales_by_product.plot(kind='bar')
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()