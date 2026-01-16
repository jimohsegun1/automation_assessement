'''
You’re given a CSV file containing Customer Name, Order Date, Order Amount, and Country. Your task is to:
1. Make a copy of the file.
2. Calculate the total order value for "John Doe", but only include orders greater than $100.
3. Identify the country with the highest total revenue, but only include orders where the amount is greater than $100 in your calculation.
4. Calculate the average order amount across all orders over $100
5. Create a bar chart showing total revenue by country, using only orders over $50.
Note: All numbers should be rounded to whole numbers.
Total order value for John Doe (orders > $100): 890
Country with highest total revenue (orders > $100): USA
Average order amount (orders > $100): 193
Upload a screenshot clearly showing your chart below

'''



import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = "data.csv"
df = pd.read_csv(file_path)

# 1. Make a copy of the file (dataframe copy)
df_copy = df.copy()

# Ensure Order Amount is numeric
df_copy["Order Amount"] = pd.to_numeric(df_copy["Order Amount"], errors="coerce")

# 2. Total order value for John Doe, orders > $100
john_doe_total = df_copy[
    (df_copy["Customer Name"] == "John Doe") & (df_copy["Order Amount"] > 100)
]["Order Amount"].sum()

# 3. Country with highest total revenue, orders > $100
country_revenue_over_100 = (
    df_copy[df_copy["Order Amount"] > 100]
    .groupby("Country")["Order Amount"]
    .sum()
)
top_country = country_revenue_over_100.idxmax()
top_country_revenue = country_revenue_over_100.max()

# 4. Average order amount across all orders > $100
average_order_over_100 = df_copy[df_copy["Order Amount"] > 100]["Order Amount"].mean()

# 5. Bar chart: total revenue by country, orders > $50
country_revenue_over_50 = (
    df_copy[df_copy["Order Amount"] > 50]
    .groupby("Country")["Order Amount"]
    .sum()
)

print("Total order value for John Doe (orders > $100):", john_doe_total)
print("Country with highest total revenue (orders > $100):", top_country)
print("Total revenue for the top country (orders > $100):", top_country_revenue)
print("Average order amount (orders > $100):", average_order_over_100)

plt.figure()
country_revenue_over_50.plot(kind="bar")
plt.title("Total Revenue by Country (Orders > $50)")
plt.xlabel("Country")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.show()



john_doe_total, top_country, top_country_revenue, average_order_over_100