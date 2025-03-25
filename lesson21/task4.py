import pandas as pd
import matplotlib.pyplot as plt

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df = pd.DataFrame(data4)
# 1
print((df['Quantity'] * df['Total_Price']).sum())
# 2
print('=========================================')
print(df[df['Quantity'] == df['Quantity'].max()])
# 3
print('=========================================')
print(df['Quantity'].mean())
# 4
df['Product'].value_counts().plot(kind='pie', autopct='%1.1f%%')
for i, v in enumerate(df['Product'].value_counts()):
    plt.text(i, v + 0.2, str(v))
plt.show()
