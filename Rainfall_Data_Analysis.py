
import csv
import numpy as np

# 1. Create a sample rainfall CSV file
data = [
    ["2026-01-01", "Kochi", 25],
    ["2026-01-02", "Kochi", 40],
    ["2026-01-03", "Kochi", 30],
    ["2026-01-01", "Thrissur", 15],
    ["2026-01-02", "Thrissur", 35],
    ["2026-01-03", "Thrissur", 20]
]

with open("rainfall.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Station", "Rainfall (mm)"])
    writer.writerows(data)

print("Rainfall CSV file created!")


# 2. Read rainfall data from CSV file
dates = []
stations = []
rainfall = []

with open("rainfall.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        dates.append(row["Date"])
        stations.append(row["Station"])
        rainfall.append(float(row["Rainfall (mm)"]))

# Convert rainfall list into NumPy array
rainfall = np.array(rainfall)


# 3. Calculate average rainfall per station
print("\nAverage Rainfall per Station:")

unique_stations = set(stations)

average_results = []

for station in unique_stations:
    values = []

    for i in range(len(stations)):
        if stations[i] == station:
            values.append(rainfall[i])

    avg = np.mean(values)

    print(station, ":", avg, "mm")

    average_results.append([station, avg])


# 4. Find maximum rainfall and its date
max_index = np.argmax(rainfall)

max_rainfall = rainfall[max_index]
max_date = dates[max_index]
max_station = stations[max_index]

print("\nMaximum Rainfall:")
print("Rainfall:", max_rainfall, "mm")
print("Date:", max_date)
print("Station:", max_station)


# 5. Calculate standard deviation
std_dev = np.std(rainfall)

print("\nStandard Deviation:", std_dev)


# 6. Save results into a new CSV file
with open("rainfall_results.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Result", "Value"])

    for station, avg in average_results:
        writer.writerow(["Average Rainfall - " + station, avg])

    writer.writerow(["Maximum Rainfall", max_rainfall])
    writer.writerow(["Maximum Rainfall Date", max_date])
    writer.writerow(["Maximum Rainfall Station", max_station])
    writer.writerow(["Standard Deviation", std_dev])

print("\nResults saved to rainfall_results.csv")

