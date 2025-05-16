import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data into a Pandas DataFrame
# Assuming the data is in a CSV file named "sales_data.csv"
# You can replace this with the actual path to your data file
try:
    df = pd.read_csv("sales_data.csv")
except FileNotFoundError:
    # Create a dummy DataFrame if the file is not found
    df = pd.DataFrame({
        'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03', '2023-01-03'],
        'Product': ['A', 'B', 'A', 'B', 'A', 'B'],
        'Quantity': [10, 15, 20, 25, 30, 35],
        'Revenue': [100, 150, 200, 250, 300, 350]
    })
    print("Warning: sales_data.csv not found. Using dummy data.")

# 2. Explore the data
print("First 5 rows of the data:")
print(df.head())

print("\nSummary statistics of the numerical columns:")
print(df.describe())

print("\nData types of the columns and information about missing values:")
print(df.info())

# 3. Calculate total revenue per product
total_revenue_per_product = df.groupby('Product')['Revenue'].sum()
print("\nTotal revenue per product:")
print(total_revenue_per_product)

# 4. Create a bar chart to visualize the total revenue per product
plt.figure(figsize=(10, 6))  # Adjust figure size for better readability
total_revenue_per_product.plot(kind='bar', color='skyblue')
plt.title('Total Revenue per Product')
plt.xlabel('Product')
plt.ylabel('Total Revenue')
plt.xticks(rotation=0)  # Rotate x-axis labels if needed
plt.grid(axis='y', linestyle='--')  # Add gridlines for better readability
plt.tight_layout()  # Adjust layout to prevent labels from overlapping
plt.show()

# 5. Create a line plot to visualize the trend of revenue over time
# Convert 'Date' to datetime if it's not already
df['Date'] = pd.to_datetime(df['Date'])

# Aggregate revenue by date
revenue_by_date = df.groupby('Date')['Revenue'].sum().reset_index()

plt.figure(figsize=(10, 6))
plt.plot(revenue_by_date['Date'], revenue_by_date['Revenue'], marker='o', linestyle='-', color='salmon')  # Added marker
plt.title('Revenue Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Total Revenue')
plt.grid(True, linestyle='--')
plt.tight_layout()
plt.show()
