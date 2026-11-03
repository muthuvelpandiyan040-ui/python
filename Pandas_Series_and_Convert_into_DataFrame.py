import pandas as pd

# Create individual Pandas Series
Name = pd.Series(['John', 'David', 'Mary', 'Alex', 'Sara'])
Age = pd.Series([20, 21, 22, 20, 23])
Course = pd.Series(['MCA', 'MBA', 'BCA', 'MCA', 'BBA'])
Marks = pd.Series([75, 35, 85, 30, 60])

# Convert Series into DataFrame
df = pd.DataFrame({
    'Name': Name,
    'Age': Age,
    'Course': Course,
    'Marks': Marks
})

print("Student Details:")
print(df)

# Add Pass or Fail column
df['Result'] = df['Marks'].apply(
    lambda x: 'Pass' if x >= 40 else 'Fail'
)

print("\nStudent Results:")
print(df)

# Display only passed students
passed_students = df[df['Result'] == 'Pass']

print("\nPassed Students:")
print(passed_students)