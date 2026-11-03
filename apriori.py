pip install pandas
pip install openpyxl
pip install mlxtend


# Import libraries
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# 1. Load Excel dataset
data = pd.read_excel("groceries.xlsx", header=None)

transactions = data.values.tolist()

# Remove empty values
transactions = [
    [str(item).strip() for item in row if pd.notna(item)]
    for row in transactions
]

print("Dataset Loaded Successfully!")
print("Total Transactions:", len(transactions))

# 2. Convert data into one-hot encoding
te = TransactionEncoder()
encoded = te.fit(transactions).transform(transactions)

df = pd.DataFrame(encoded, columns=te.columns_)

# 3. Apply Apriori Algorithm
frequent_items = apriori(
    df,
    min_support=0.01,
    use_colnames=True
)

print("\nFrequent Itemsets:")
print(frequent_items.sort_values(
    "support", ascending=False
).head(10))

# 4. Find Most Frequent Items
print("\nMost Frequent Items:")
print(df.sum().sort_values(
    ascending=False
).head(10))

# 5. Generate Association Rules
rules = association_rules(
    frequent_items,
    metric="confidence",
    min_threshold=0.1
)

print("\nAssociation Rules:")
print(rules[
    ["antecedents", "consequents",
     "support", "confidence", "lift"]
].head(10))

# 6. Top 5 Rules with Highest Lift
top5 = rules.sort_values(
    "lift", ascending=False
).head(5)

print("\nTop 5 Rules with Highest Lift:")
print(top5[
    ["antecedents", "consequents",
     "support", "confidence", "lift"]
])

print("\nProgram Completed Successfully!")
