import pandas as pd
import random

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
# 1
df = df.rename(columns={'First Name': 'first_name', 'Age': 'age'})
# 2
print(df[:3])
# 3
print(f'Mean age is: {df['age'].mean()}')
# 4
print(df[['first_name', 'City']])
# 5
df['Salary'] = [random.randint(100, 500) for _ in range(len(df))]
# 6
print(df)
