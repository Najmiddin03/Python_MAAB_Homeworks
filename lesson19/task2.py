import pandas as pd

df = pd.read_csv('task\\customer_orders.csv')
# 1
sum_orders = df.groupby('CustomerID')['Quantity'].sum()
big_orders = sum_orders[sum_orders >= 20].index
result = df[df['CustomerID'].isin(big_orders)]
print(result.groupby('CustomerID').agg({'Quantity': 'sum'}))
# 2
avg_price = df.groupby('CustomerID').filter(lambda x: x['Price'].mean() >= 120)
print(avg_price.groupby('CustomerID')['Price'].mean())
# 3
total_ordered = df.groupby('Product').filter(lambda x: x['Quantity'].sum() >= 5)
total_ordered['Total price'] = total_ordered['Quantity'] * total_ordered['Price']
print(total_ordered.groupby('Product').agg({'Quantity': 'sum', 'Total price': 'sum'}))
