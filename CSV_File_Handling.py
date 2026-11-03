
import csv

# 1. Create CSV file and insert student records
students = [
    [1, "Arun", 85],
    [2, "Rahul", 90],
    [3, "Anu", 78],
    [4, "David", 95],
    [5, "Meera", 88]
]

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    # Write column headings
    writer.writerow(["Roll_No", "Name", "Marks"])

    # Insert student records
    writer.writerows(students)

print("CSV file created successfully!")


# 2. Read data from CSV file
with open("students.csv", "r") as file:

    reader = csv.DictReader(file)

    records = []

    for row in reader:
        records.append({
            "Roll_No": int(row["Roll_No"]),
            "Name": row["Name"],
            "Marks": int(row["Marks"])
        })


# Display all student records
print("\nStudent Details:")

for student in records:
    print(student)


# 3. Find student with highest marks
highest = max(records, key=lambda x: x["Marks"])

print("\nStudent with Highest Marks:")
print("Roll Number:", highest["Roll_No"])
print("Name:", highest["Name"])
print("Marks:", highest["Marks"])


# 4. Calculate average marks
total = sum(student["Marks"] for student in records)

average = total / len(records)

print("\nAverage Marks:", average)
