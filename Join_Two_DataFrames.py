import pandas as pd

# First DataFrame
exam_data1 = {
    'student_id': ['S1', 'S2', 'S3', 'S4', 'S5', 'S7'],
    'exam_id': [23, 45, 12, 67, 21, 55]
}

df1 = pd.DataFrame(exam_data1)

# Second DataFrame
exam_data2 = {
    'student_id': ['S8', 'S9', 'S10', 'S11', 'S12', 'S13'],
    'exam_id': [33, 14, 56, 83, 88, 12]
}

df2 = pd.DataFrame(exam_data2)

# Join two DataFrames along rows
result = pd.concat([df1, df2], ignore_index=True)

print("Joined DataFrame:")
print(result)

# Third DataFrame
student_data = {
    'student_id': ['S1', 'S2', 'S3', 'S4', 'S5', 'S7',
                   'S8', 'S9', 'S10', 'S11', 'S12', 'S13'],
    'name': ['John', 'David', 'Mary', 'Alex', 'Sam', 'Tom',
             'Sara', 'Anna', 'Mike', 'Paul', 'Lisa', 'Rose']
}

df3 = pd.DataFrame(student_data)

# Merge using common column student_id
merged_data = pd.merge(result, df3, on='student_id')

print("\nMerged DataFrame:")
print(merged_data)



# Join Two DataFrames with Matching Records from Both Sides




import pandas as pd

# First DataFrame
exam_data = {
    'student_id': ['S1', 'S2', 'S3', 'S4', 'S5', 'S7'],
    'exam_id': [23, 45, 12, 67, 21, 55]
}

df1 = pd.DataFrame(exam_data)

# Second DataFrame
student_data = {
    'student_id': ['S1', 'S2', 'S3', 'S8', 'S9', 'S10'],
    'name': ['John', 'David', 'Mary', 'Sara', 'Anna', 'Mike']
}

df2 = pd.DataFrame(student_data)

# Inner Join
result = pd.merge(df1, df2, on='student_id', how='inner')

print("Inner Join Result:")
print(result)