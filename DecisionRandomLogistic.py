pip install pandas numpy matplotlib seaborn scikit-learn

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score, confusion_matrix


# 1. Load Dataset
file_path = r"C:\Users\Ferci\Downloads\breast+cancer\breast-cancer.data"

columns = [
    "Class", "age", "menopause", "tumor_size",
    "inv_nodes", "node_caps", "deg_malig",
    "breast", "breast_quad", "irradiat"
]

data = pd.read_csv(
    file_path,
    header=None,
    names=columns,
    na_values="?"
)

# Remove Missing Values
data = data.dropna()

# Select 5 records from each class
data = pd.concat([
    data[data["Class"] == "recurrence-events"].head(5),
    data[data["Class"] == "no-recurrence-events"].head(5)
])

print("Dataset Loaded Successfully!")
print("Dataset Shape:", data.shape)
print(data.head(10))


# 2. Check Class Distribution
print("\nClass Distribution:")
print(data["Class"].value_counts())


# 3. Separate Features and Target
X = data.drop("Class", axis=1)

# 1 = Recurrence, 0 = No Recurrence
y = (data["Class"] == "recurrence-events").astype(int)


# 4. Convert Categorical Data into Numerical Data
X = pd.get_dummies(X, drop_first=True, dtype=int)

print("\nCategorical Data Converted!")
print("Features Shape:", X.shape)


# 5. Correlation Heatmap
plt.figure(figsize=(12, 8))

sns.heatmap(
    X.corr(),
    cmap="coolwarm",
    center=0
)

plt.title("Correlation Heatmap")
plt.show()


# 6. Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

print("\nDataset Splitting Completed!")
print("Training Data:", X_train.shape)
print("Testing Data:", X_test.shape)


# 7. Feature Scaling
scaler = StandardScaler()

X_train_scaled = pd.DataFrame(
    scaler.fit_transform(X_train),
    columns=X.columns,
    index=X_train.index
)

X_test_scaled = pd.DataFrame(
    scaler.transform(X_test),
    columns=X.columns,
    index=X_test.index
)

print("\nFeature Scaling Completed!")


# 8. Random Forest Feature Ranking
rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf.fit(X_train_scaled, y_train)

importance = pd.Series(
    rf.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

print("\nFeature Ranking:")
print(importance)


# Plot Feature Importance
importance.head(10).plot(
    kind="bar",
    figsize=(10, 5)
)

plt.title("Top 10 Important Features")
plt.ylabel("Importance")
plt.show()


# 9. Select Top 10 Features
top_features = importance.head(10).index.tolist()

print("\nSelected Features:")
print(top_features)

X_train_selected = X_train_scaled[top_features]
X_test_selected = X_test_scaled[top_features]


# 10. Define Models
models = {
    "Decision Tree": DecisionTreeClassifier(
        random_state=42,
        class_weight="balanced"
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        class_weight="balanced"
    ),

    "Logistic Regression": LogisticRegression(
        max_iter=1000,
        class_weight="balanced"
    )
}


# 11. Train and Evaluate Models
results = []
trained_models = {}

for feature_type, train_data, test_data in [
    ("All Features", X_train_scaled, X_test_scaled),
    ("Top 10 Features", X_train_selected, X_test_selected)
]:

    for name, model in models.items():

        model.fit(train_data, y_train)

        prediction = model.predict(test_data)

        cm = confusion_matrix(
            y_test,
            prediction,
            labels=[0, 1]
        )

        tn, fp, fn, tp = cm.ravel()

        accuracy = accuracy_score(y_test, prediction)

        recall = recall_score(
            y_test,
            prediction,
            zero_division=0
        )

        results.append([
            feature_type,
            name,
            accuracy,
            recall,
            fn
        ])

        trained_models[(feature_type, name)] = model

        print("\n", feature_type, "-", name)
        print("Accuracy:", accuracy)
        print("Recall:", recall)
        print("Confusion Matrix:\n", cm)
        print("False Negatives:", fn)


# 12. Compare Model Performance
comparison = pd.DataFrame(
    results,
    columns=[
        "Features",
        "Model",
        "Accuracy",
        "Recall",
        "False Negatives"
    ]
)

print("\n--- MODEL PERFORMANCE COMPARISON ---")
print(comparison)


# 13. Find Model with Minimum False Negatives
selected_results = comparison[
    comparison["Features"] == "Top 10 Features"
]

best_row = selected_results.sort_values(
    ["False Negatives", "Recall", "Accuracy"],
    ascending=[True, False, False]
).iloc[0]

best_model_name = best_row["Model"]

print("\nModel with Minimum False Negatives:")
print(best_model_name)
print("False Negatives:", best_row["False Negatives"])


# 14. Confusion Matrix of Best Model
best_model = trained_models[
    ("Top 10 Features", best_model_name)
]

prediction = best_model.predict(X_test_selected)

cm = confusion_matrix(
    y_test,
    prediction,
    labels=[0, 1]
)

plt.figure(figsize=(6, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["No Recurrence", "Recurrence"],
    yticklabels=["No Recurrence", "Recurrence"]
)

plt.title("Confusion Matrix - Best Model")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()


# 15. Predict New Sample
new_sample = X_test_selected.iloc[[0]]

result = best_model.predict(new_sample)

if result[0] == 1:
    print("\nPredicted Result: Recurrence")
else:
    print("\nPredicted Result: No Recurrence")


print("\nProgram Completed Successfully!")
