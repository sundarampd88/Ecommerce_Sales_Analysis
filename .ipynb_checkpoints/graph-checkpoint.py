import pandas as pd

import matplotlib.pyplot as plt
df = pd.read_csv("cleaned_sales.csv")
df["OrderDate"] = pd.to_datetime(df["OrderDate"])

product_date_sales = df.groupby(
    ["OrderDate", "Product"]
)["Total_Sales"].sum()

# Sab bars normal color
colors = ["steelblue"] * len(product_date_sales)

# Laptop wale bars green
for i, item in enumerate(product_date_sales.index):
    if item[1] == "Laptop":
        colors[i] = "green"

product_date_sales.plot(
    kind="bar",
    color=colors
)

plt.title("Product-wise Sales by Date")
plt.xlabel("Date and Product")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()