import pandas as pd

# Create DataFrame
data = {
    'Name': ['Alberto Franco', 'Gino Mcneill',
             'Ryan Parkes', 'Eesha Hinton',
             'Syed Wharton'],
    'Age': [18, 22, 40, 50, 80]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Convert Age into categories
bins = [0, 18, 40, 60, 100]
labels = ['Child', 'Young', 'Middle Age', 'Senior']

df['Age_Category'] = pd.cut(
    df['Age'],
    bins=bins,
    labels=labels,
    include_lowest=True
)

print("\nDataFrame after converting Age into Categories:")
print(df)