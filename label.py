import pandas as pd
 
df = pd.read_csv('~/sotuken/organelles.csv', encoding='shift-jis')
df2 = df['Organism Groups']
print(df2)
df2.to_csv('~/sotuken/label.csv',header=True,index=False)
print(df2[1])