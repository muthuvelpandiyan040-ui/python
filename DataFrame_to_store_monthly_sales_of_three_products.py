import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Product A': [100, 150, 120, 180, 200, 170],
    'Product B': [120, 130, 140, 160, 180, 190],
    'Product C': [90, 110, 130, 150, 170, 160]
}

df = pd.DataFrame(data)

# Display DataFrame
print("Monthly Sales:")
print(df)

# Calculate total sales for each month
df['Total Sales'] = df[['Product A', 'Product B',
                        'Product C']].sum(axis=1)

print("\nTotal Sales:")
print(df[['Month', 'Total Sales']])

# Find month with highest sales
max_month = df.loc[df['Total Sales'].idxmax(), 'Month']

print("\nMonth with Highest Sales:", max_month)

# Plot bar chart
df.plot(x='Month', y=['Product A', 'Product B', 'Product C'],
        kind='bar')

plt.title("Monthly Sales of Three Products")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid(axis='y')

plt.show()