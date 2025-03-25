import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.float_format = '{:,.2f}'.format
data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df = pd.DataFrame(data2)
df.set_index('Date', inplace=True)
# 1
print(df.sum())
# 2
print(df[df.sum(axis=1) == df.sum(axis=1).max()])
# 3
print(df.pct_change() * 100)
# 4
df.plot(figsize=(10, 8))
plt.ylabel('Products sold')
plt.show()
