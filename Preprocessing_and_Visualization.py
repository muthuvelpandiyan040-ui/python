pip install pandas numpy matplotlib seaborn scikit-learn


# Install required libraries (run once in Jupyter)
# !pip install pandas numpy matplotlib seaborn scikit-learn

# ==========================================
# 1. IMPORT LIBRARIES
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# ==========================================
# 2. LOAD DATASET
# ==========================================

df = pd.read_csv(r"C:\Users\Ferci\Downloads\Data .csv")

print("Dataset Loaded Successfully!")
print("\nFirst 5 Records:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

# ==========================================
# 3. CHECK MISSING VALUES
# ==========================================

print("\nMissing Values:")
print(df.isnull().sum())

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

# ==========================================
# 4. VISUALIZE NUMERICAL DATA
# ==========================================

df.hist(figsize=(10, 6), bins=10)

plt.suptitle("Feature Distribution")
plt.tight_layout()
plt.show()

# ==========================================
# 5. SEPARATE FEATURES AND TARGET
# ==========================================

X = df.drop("Purchased", axis=1)
y = df["Purchased"]

# Remove rows with missing target values
valid = y.notna()

X = X.loc[valid].copy()
y = y.loc[valid].copy()

# ==========================================
# 6. IDENTIFY NUMERICAL AND CATEGORICAL COLUMNS
# ==========================================

num_cols = X.select_dtypes(include=np.number).columns.tolist()

cat_cols = X.select_dtypes(exclude=np.number).columns.tolist()

print("\nNumerical Columns:", num_cols)
print("Categorical Columns:", cat_cols)

# ==========================================
# 7. SPLIT DATASET
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)

# ==========================================
# 8. HANDLE MISSING VALUES AND ENCODE DATA
# ==========================================

# Numerical preprocessing
num_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler())
])

# Categorical preprocessing
cat_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", __import__("sklearn").preprocessing.OneHotEncoder(
        handle_unknown="ignore"
    ))
])

# Combine preprocessing
preprocessor = ColumnTransformer([
    ("numerical", num_pipeline, num_cols),
    ("categorical", cat_pipeline, cat_cols)
])

# Fit only on training data
X_train_processed = preprocessor.fit_transform(X_train)

# Transform testing data
X_test_processed = preprocessor.transform(X_test)

# Convert to DataFrames
feature_names = preprocessor.get_feature_names_out()

X_train_processed = pd.DataFrame(
    X_train_processed,
    columns=feature_names,
    index=X_train.index
)

X_test_processed = pd.DataFrame(
    X_test_processed,
    columns=feature_names,
    index=X_test.index
)

# ==========================================
# 9. ENCODE TARGET COLUMN
# ==========================================

le = LabelEncoder()

y_train_encoded = le.fit_transform(y_train)
y_test_encoded = le.transform(y_test)

print("\nTarget Encoding:")
print(dict(zip(le.classes_, le.transform(le.classes_))))

# ==========================================
# 10. DISPLAY PREPROCESSED DATA
# ==========================================

print("\nProcessed Training Dataset:")
print(X_train_processed.head())

print("\nProcessed Testing Dataset:")
print(X_test_processed.head())

print("\nMissing Values After Preprocessing:")
print(X_train_processed.isnull().sum())

# ==========================================
# 11. CORRELATION HEATMAP
# ==========================================

plt.figure(figsize=(10, 7))

sns.heatmap(
    X_train_processed.corr(),
    cmap="coolwarm",
    annot=True,
    fmt=".2f"
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# ==========================================
# 12. VISUALIZE CATEGORICAL DATA
# ==========================================

for col in cat_cols:

    plt.figure(figsize=(6, 4))

    sns.countplot(data=df, x=col)

    plt.title("Distribution of " + col)
    plt.xlabel(col)
    plt.ylabel("Count")

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# ==========================================
# 13. VISUALIZE TARGET DISTRIBUTION
# ==========================================

plt.figure(figsize=(6, 4))

sns.countplot(x=y)

plt.title("Purchased Class Distribution")
plt.xlabel("Purchased")
plt.ylabel("Count")

plt.tight_layout()
plt.show()

# ==========================================
# 14. SAVE PREPROCESSED DATASET
# ==========================================

train_output = X_train_processed.copy()
test_output = X_test_processed.copy()

train_output["Purchased"] = y_train_encoded
test_output["Purchased"] = y_test_encoded

train_output.to_csv("Preprocessed_Train.csv", index=False)
test_output.to_csv("Preprocessed_Test.csv", index=False)

print("\n===================================")
print("PREPROCESSING COMPLETED SUCCESSFULLY!")
print("===================================")

print("\nSaved Files:")
print("1. Preprocessed_Train.csv")
print("2. Preprocessed_Test.csv")
