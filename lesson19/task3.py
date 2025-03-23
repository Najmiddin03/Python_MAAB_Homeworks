import sqlite3
import pandas as pd

pd.set_option('display.width', None)
pd.options.display.float_format = '{:,.2f}'.format

conn = sqlite3.connect("task\\population.db")
cursor = conn.cursor()
df = pd.read_sql_query('select * from population', conn)
conn.close()
salary_bands = [
    ('till $200,000', 0, 200000),
    ('$200,001 - $400,000', 200001, 400000),
    ('$400,001 - $600,000', 400001, 600000),
    ('$600,001 - $800,000', 600001, 800000),
    ('$800,001 - $1,000,000', 800001, 1000000),
    ('$1,000,001 - $1,200,000', 1000001, 1200000),
    ('$1,200,001 - $1,400,000', 1200001, 1400000),
    ('$1,400,001 - $1,600,000', 1400001, 1600000),
    ('$1,600,001 - $1,800,000', 1600001, 1800000),
    ('$1,800,001 and over', 1800001, float('inf'))
]


def categorize_salary(salary):
    for band, low, high in salary_bands:
        if low <= salary <= high:
            return band
    return None


df['Salary band'] = df['salary'].apply(categorize_salary)
salary_distribution = df.groupby('Salary band').size().reset_index(name='Num of people')
total_population = len(df)
salary_distribution['Percentage'] = salary_distribution['Num of people'] / total_population * 100
salary_distribution['Percentage'] = salary_distribution['Percentage'].astype(float)
# 1
print(salary_distribution)
# 2
print(df.groupby('Salary band')['salary'].mean().reset_index(name='Avg salary'))
# 3
print(df.groupby('Salary band')['salary'].median().reset_index(name='Median salary'))

# For each state
state_distribution = df.groupby('state').size().reset_index(name="Num of people")
state_distribution['Percentage'] = state_distribution['Num of people'] / total_population * 100
# 1
print(state_distribution.sort_values(by='Num of people'))
# 2
print(df.groupby('state')['salary'].mean().reset_index(name='Avg salary'))
# 3
print(df.groupby('state')['salary'].median().reset_index(name='Median salary'))
