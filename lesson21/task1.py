import pandas as pd
import matplotlib.pyplot as plot

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df = pd.DataFrame(data1)

df.set_index('Student_ID', inplace=True)
# 1
df['Mean score'] = df.mean(axis=1)
print(df['Mean score'])
# 2
print(df[df['Mean score'] == df['Mean score'].max()])
# 3
df['Total score'] = df.sum(axis=1)
print(df)
# 4
plot_data = df.mean()
plot_data[['Math', 'English', 'Science']].plot(kind='bar', figsize=(10, 8))
plot.xlabel('Subjects')
plot.ylabel('Average score')
plot.show()
