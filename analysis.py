import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Student.csv")

data['Total'] = data['Maths'] + data['Physics'] + data['Chemistry']

print(data.head())

print(data.loc[data['Total'].idxmax()])

avg = data['Total'].mean()
print(data[data['Total'] > avg])

plt.hist(data['Total'])
plt.show()
