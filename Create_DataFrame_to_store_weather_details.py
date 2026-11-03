import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday'],
    'Temperature': [30, 32, 29, 31, 28, 33, 30],
    'Humidity': [70, 65, 75, 68, 80, 60, 72],
    'Rainfall': [2, 0, 5, 1, 10, 0, 3]
}

df = pd.DataFrame(data)

# Display DataFrame
print("Weather Details:")
print(df)

# Calculate average temperature
avg_temp = df['Temperature'].mean()
print("\nAverage Temperature:", avg_temp)

# Calculate total rainfall
total_rainfall = df['Rainfall'].sum()
print("Total Rainfall:", total_rainfall)

# Plot Temperature vs Day
plt.plot(df['Day'], df['Temperature'], marker='o')

plt.title("Temperature vs Day")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.grid()

plt.show()