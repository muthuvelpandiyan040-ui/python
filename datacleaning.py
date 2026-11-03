pip install pandas numpy


# Import libraries
import pandas as pd
import numpy as np

# 1. Load Dataset
df = pd.read_csv("dirtydata.csv")

print("Original Dataset:")
print(df)

print("\nDataset Information:")
print(df.info())

# 2. Check Empty Cells
print("\nEmpty Cells:")
print(df.isnull().sum())

# 3. Remove Rows with Empty Cells using dropna()
drop_data = df.dropna()

print("\nAfter dropna():")
print(drop_data)

# 4. Fill Empty Cells using Mean, Median and Mode
df_mean = df.copy()
df_median = df.copy()
df_mode = df.copy()

# Mean
for col in df_mean.select_dtypes(include=np.number).columns:
    df_mean[col] = df_mean[col].fillna(df_mean[col].mean())

print("\nAfter Filling with Mean:")
print(df_mean)

# Median
for col in df_median.select_dtypes(include=np.number).columns:
    df_median[col] = df_median[col].fillna(df_median[col].median())

print("\nAfter Filling with Median:")
print(df_median)

# Mode (works for numeric and text columns)
for col in df_mode.columns:
    if not df_mode[col].mode().empty:
        df_mode[col] = df_mode[col].fillna(df_mode[col].mode()[0])

print("\nAfter Filling with Mode:")
print(df_mode)

# 5. Handle Wrong Data Format
# Convert numeric columns into proper numeric format
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='ignore')

# Convert date column if available
for col in df.columns:
    if 'date' in col.lower():
        df[col] = pd.to_datetime(df[col], errors='coerce')

print("\nAfter Correcting Data Format:")
print(df.info())

# 6. Handle Wrong Data
# Remove unwanted spaces from text columns
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.strip()

# Example: Replace incorrect values
# df['ColumnName'] = df['ColumnName'].replace('wrong', 'correct')

print("\nAfter Handling Wrong Data:")
print(df)

# 7. Find Duplicate Rows
print("\nDuplicate Rows:")
print(df[df.duplicated()])

# 8. Remove Duplicate Rows
df = df.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(df)

# 9. Save Cleaned Dataset
df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned Dataset Saved Successfully!")
