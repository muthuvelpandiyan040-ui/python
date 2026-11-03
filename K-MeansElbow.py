pip install pandas numpy matplotlib seaborn scikit-learn

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# 1. Load Iris dataset (without target label)
iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)

print("Dataset Loaded Successfully!")
print(df.head())

# 2. Visualize feature distributions
df.hist(figsize=(10, 8))
plt.suptitle("Feature Distributions")
plt.tight_layout()
plt.show()

# 3. Standardize the dataset
scaler = StandardScaler()
X = scaler.fit_transform(df)

print("Dataset Standardized Successfully!")

# 4. Apply K-Means for k = 2, 3, 4
for k in [2, 3, 4]:

    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)

    clusters = kmeans.fit_predict(X)

    print("\nK =", k)
    print("Cluster Labels:", clusters)

# 5. Elbow Method
wcss = []

for k in range(1, 11):

    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)

    kmeans.fit(X)

    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.show()

# 6. PCA for 2D visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Apply K-Means with k = 3
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

clusters = kmeans.fit_predict(X)

# Visualize clusters
plt.figure(figsize=(8, 6))

plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c=clusters,
    cmap='viridis'
)

plt.title("K-Means Clustering using PCA")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.show()

print("\nClustering Completed Successfully!")
