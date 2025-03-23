import pandas as pd

# 1
data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
        'Sales': [5000, 6000, 7500, 8000],
        'Expenses': [3000, 3500, 4000, 4500]}
df = pd.DataFrame(data)
# 2
print(f"Maximum sales: {df['Sales'].max()}")
print(f"Maximum expenses: {df['Expenses'].max()}")
# 3
print(f"Minimum sales: {df['Sales'].min()}")
print(f"Minimum expenses: {df['Expenses'].min()}")
# 4
print(f"Avg sales: {df['Sales'].mean()}")
print(f"Avg expenses: {df['Expenses'].mean()}")