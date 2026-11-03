pip install pandas matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame
data = {
    'a': [2, 4, 6, 8, 10],
    'b': [4, 2, 4, 2, 2],
    'c': [8, 3, 7, 6, 4],
    'd': [5, 4, 4, 4, 3],
    'e': [7, 2, 7, 8, 3]
}

df = pd.DataFrame(data)

# Create bar plot
df.plot(kind='bar')

# Add title and labels
plt.title('Bar Plot')
plt.xlabel('Index')
plt.ylabel('Values')

# Display graph
plt.show()