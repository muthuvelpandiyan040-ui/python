import pandas as pd

# Create DataFrame
data = {
    'EmployeeID': [101, 102, 103, 104, 105, 106],
    'Name': ['John', 'David', 'Mary', 'Alex', 'Sara', 'Peter'],
    'Department': ['IT', 'HR', 'IT', 'HR', 'Finance', 'Finance'],
    'Salary': [50000, 40000, 60000, 45000, 55000, 65000]
}

df = pd.DataFrame(data)

# Display DataFrame
print("Employee Details:")
print(df)

# Average salary per department
avg_salary = df.groupby('Department')['Salary'].mean()

print("\nAverage Salary per Department:")
print(avg_salary)

# Employee with highest salary
highest = df.loc[df['Salary'].idxmax()]

print("\nEmployee with Highest Salary:")
print(highest)