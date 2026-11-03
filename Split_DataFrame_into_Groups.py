import pandas as pd

# Create DataFrame
data = {
    'Id': [1, 2, 1, 1, 2, 1, 2],
    'type': [10, 15, 11, 20, 21, 12, 14],
    'book': ['Math', 'English', 'Physics', 'Math',
             'English', 'Physics', 'English']
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Group by all columns
grouped = df.groupby(['Id', 'type', 'book'])

# Calculate value counts
result = df.value_counts()

print("\nGroupBy Value Counts:")
print(result)