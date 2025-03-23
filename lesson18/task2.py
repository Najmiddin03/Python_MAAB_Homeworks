from xml.dom.minidom import NamedNodeMap

import pandas as pd

pd.set_option('display.width', None)

df = pd.read_csv("task\\titanic.csv")
# 1
print('Task 1')
filter0 = df['Sex'] == 'female'
filter1 = df['Pclass'] == 1
filter2 = df['Age'].between(20, 30)
print(df[filter0 & filter1 & filter2])
# 2
print('Task 2')
print(df[df['Fare'] > 100])
# 3
print('Task 3')
filter3 = df['Survived'] == 1
filter4 = df['SibSp'] == 0
filter5 = df['Parch'] == 0
print(df[filter3 & filter4 & filter5])
# 4
print('Task 4')
filter6 = df['Embarked'] == 'C'
filter7 = df['Fare'] > 50
print(df[filter6 & filter7])
# 5
print('Task 5')
print(df[~(filter4 | filter5)])
# 6
print('Task 6')
filter8 = df['Age'] <= 15
print(df[~filter3 & filter8])
# 7
print('Task 7')
filter9 = df['Cabin'].isna()
filter10 = df['Fare'] > 200
print(df[~filter9 & filter10])
# 8
print('Task 8')
print(df[df['PassengerId'] % 2 == 1])
# 9
print('Task 9')
ticket_counts = df['Ticket'].value_counts()
unique_tickets = ticket_counts[ticket_counts == 1].index
print(df[df['Ticket'].isin(unique_tickets)])
# 10
print('Task 10')
print(df[df['Name'].str.contains('Miss') & filter1])
