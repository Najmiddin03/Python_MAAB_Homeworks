import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.float_format = '{:,.2f}'.format
data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df = pd.DataFrame(data3)

# 1
print(df.groupby('Department')['Salary'].mean())
# 2
print('=========================================')
print(df[df['Experience (Years)'] == df['Experience (Years)'].max()])
# 3
df['Salary increase'] = df['Salary'] / df['Salary'].min() * 100 - 100
print('=========================================')
print(df['Salary increase'])
# 4
df['Department'].value_counts().plot(kind='bar')
for i, v in enumerate(df['Department'].value_counts()):
    plt.text(i, v + 0.2, str(v))
plt.show()
