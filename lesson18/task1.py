import pandas as pd

df = pd.read_csv('task\\stackoverflow_qa.csv')
# 1
df['creationdate'] = pd.to_datetime(df['creationdate'])
print(df[df['creationdate'].dt.year < 2014])
# 2
print(df[df['score'] > 50])
# 3
print(df[df['score'].between(50, 100)])
# 4
filter0 = df['ans_name'] == 'Scott Boston'
print(df[filter0])
# 6
filter1 = df['creationdate'] >= '2014-03-01'
filter2 = df['creationdate'] <= '2014-10-31'
filer3 = df['score'] < 5
filer4 = df['ans_name'] == 'Unutbu'
print(df[filter1 & filter2 & filer3 & filer4])
# 7
filter5 = df['score'].between(5, 10)
filter6 = df['viewcount'] > 10000
print(df[filter5 | filter6])
# 8
print(df[~filter0])
