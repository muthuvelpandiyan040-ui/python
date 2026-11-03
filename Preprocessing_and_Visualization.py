pip install pandas numpy matplotlib seaborn scikit-learn


# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

# 1. Load Dataset
df = pd.read_csv("Data.csv")

print("Dataset Loaded Successfully!")
print(df.head())

# 2. Visualize Dataset
# Histogram
df.hist(figsize=(10, 8))
plt.suptitle("Feature Distribution")
plt.tight_layout()
plt.show()

# Count missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 3. Separate Features and Target
X = df.iloc[:, :-1].copy()
y = df.iloc[:, -1].copy()

# Remove rows with missing target values
valid = y.notna()
X = X.loc[valid]
y = y.loc[valid]

# 4. Identify Numerical and Categorical Columns
num_cols = X.select_dtypes(include=np.number).columns
cat_cols = X.select_dtypes(exclude=np.number).columns

# 5. Handle Missing Values
num_imputer = SimpleImputer(strategy="mean")
cat_imputer = SimpleImputer(strategy="most_frequent")

X[num_cols] = num_imputer.fit_transform(X[num_cols])
X[cat_cols] = cat_imputer.fit_transform(X[cat_cols])

print("\nMissing Values Handled!")
print(X.isnull().sum())

# 6. Encode Categorical Data
X = pd.get_dummies(X, columns=cat_cols, dtype=int)

# Encode Target Column
le = LabelEncoder()
y = le.fit_transform(y)

print("\nCategorical Data Encoded!")
print(X.head())

# 7. Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

print("\nScaled Dataset:")
print(X_scaled.head())

# 8. Correlation Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(X_scaled.corr(), cmap="coolwarm", annot=False)
plt.title("Correlation Heatmap")
plt.show()

# 9. Visualize Categorical Data
for col in cat_cols:
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x=col)
    plt.title("Distribution of " + col)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# 10. Visualize Target Data
plt.figure(figsize=(6, 4))
sns.countplot(x=y)
plt.title("Target Class Distribution")
plt.xlabel("Target Class")
plt.show()

# 11. Save Preprocessed Dataset
X_scaled["Target"] = y
X_scaled.to_csv("Preprocessed_Data.csv", index=False)

print("\nPreprocessing Completed Successfully!")
print("Saved as Preprocessed_Data.csv")
