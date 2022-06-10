import pandas as pd
 
df = pd.read_csv('./test.csv', encoding='shift-jis')
df2 = df['test1']
print(df2)
df2.to_csv('./output.csv',header=True,index=False)