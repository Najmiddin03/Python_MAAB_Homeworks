import pandas as pd

df = pd.read_csv('task\\sales_data.csv')
# 1
total_sales = df.groupby('Category')['Quantity'].sum()
average_price = df.groupby('Category')['Price'].mean()
max_sales = df.groupby('Category')['Quantity'].max()
print(total_sales)
print(average_price)
print(max_sales)
# 2
top_product = df.loc[df.groupby('Category')['Quantity'].idxmax()]
print(top_product)
# 3
df['Total sales'] = df["Quantity"] * df['Price']
print(df.loc[df.groupby('Category')['Total sales'].idxmax()])
