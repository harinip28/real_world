import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("REAL-WORLD DATA ANALYSIS PROJECT")

# Load dataset
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Display dataset
print("\nFirst 5 Records:")
print(df.head())

# Dataset information
print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
df.info()

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicates
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Data cleaning
df = df.drop_duplicates()

df["Order Date"] = pd.to_datetime(
    df["Order Date"], errors="coerce"
)

df = df.dropna(subset=["Order Date", "Sales", "Profit"])

print("\nData Cleaning Completed!")

# Statistical analysis
print("\nStatistical Summary:")
print(df[["Sales", "Profit", "Quantity"]].describe())

# Total sales and profit
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

print("\nTotal Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))

# Category analysis
category_sales = df.groupby("Category")["Sales"].sum()

print("\nSales by Category:")
print(category_sales)

# Region analysis
region_profit = df.groupby("Region")["Profit"].sum()

print("\nProfit by Region:")
print(region_profit)

# Customer segment analysis
segment_sales = df.groupby("Segment")["Sales"].sum()

print("\nSales by Customer Segment:")
print(segment_sales)

# Monthly sales analysis
df["Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

# Create folder for graphs
os.makedirs("Visualizations", exist_ok=True)

# Graph 1: Sales by Category
plt.figure(figsize=(7, 5))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("Visualizations/category_sales.png")
plt.show()

# Graph 2: Profit by Region
plt.figure(figsize=(7, 5))
region_profit.plot(kind="bar")
plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.tight_layout()
plt.savefig("Visualizations/region_profit.png")
plt.show()

# Graph 3: Monthly Sales Trend
plt.figure(figsize=(10, 5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Visualizations/monthly_sales.png")
plt.show()

# Graph 4: Sales by Customer Segment
plt.figure(figsize=(7, 5))
segment_sales.plot(kind="bar")
plt.title("Sales by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("Visualizations/segment_sales.png")
plt.show()

# Project findings
print("\n========== PROJECT FINDINGS ==========")

print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))

print("Highest Sales Category:", category_sales.idxmax())
print("Most Profitable Region:", region_profit.idxmax())
print("Highest Sales Customer Segment:", segment_sales.idxmax())
print("Best Sales Month:", monthly_sales.idxmax())

print("\nREAL-WORLD DATA ANALYSIS COMPLETED!")