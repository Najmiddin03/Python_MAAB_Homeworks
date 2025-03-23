import pandas as pd

# 1
data = {'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
        'Jan': [1200, 200, 300, 150],
        'Feb': [1300, 220, 320, 160],
        'Mar': [1400, 240, 330, 170],
        'Apr': [1500, 250, 350, 180]}
df = pd.DataFrame(data)
df.set_index('Category', inplace=True)
# 2
print('Max')
print(df.max(axis=1))
# 3
print('Min')
print(df.min(axis=1))
# 4
print('Avg')
print(df.mean(axis=1))
