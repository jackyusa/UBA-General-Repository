from contextlib import nullcontext
from re import A
import pandas as pd
import numpy as np
from pandas import Series
import matplotlib.pyplot as plt

df = pd.read_csv("input.csv", index_col=0)

# -------------------------- OUTPUT 1
df = df.filter(['Matches'])
df['Matches'] = df['Matches'].str.replace("[","",regex=True)
df['Matches'] = df['Matches'].str.replace("]","",regex=True)

df['Matches'] = df['Matches'].str.split(';',regex=True)

df = df.explode('Matches')

df['Matches'].replace('', np.nan, inplace=True)
df.dropna(subset=['Matches'], inplace=True)

df['MatchesSplit'] = df['Matches'].str.split(' - ')
df['Matches'] = df['Matches'].str.split(' - ')

for x in range(0,df.shape[0]):
    df['Matches'].values[x].pop()
    df['Matches'].values[x] = ''.join(df['Matches'].values[x])
    df['MatchesSplit'].values[x] = df['MatchesSplit'].values[x][-1:]
    df['MatchesSplit'].values[x] = ''.join(df['MatchesSplit'].values[x])

a = open('output1.csv', "w")
a.truncate()
a.close()
df = df.reset_index(drop=True)
df.to_csv('output1.csv',index=False)

# -------------------------- OUTPUT 2
df['counts'] = df['MatchesSplit'].map(df['MatchesSplit'].value_counts())
#df1 = df['MatchesSplit'].value_counts(sort=False)
df = df.drop_duplicates(['MatchesSplit'])

# this below code is for clearing the file
b = open('output2.csv', "w")
b.truncate()
b.close()
df = df.reset_index(drop=True)
df.to_csv('output2.csv',index=False)

# -------------------------- OUTPUT 3
df2 = df.sort_values(['counts'],ascending=False)
dfFinal = df2.head(20)
c = open('output3.csv', "w")
c.truncate()
c.close()
dfFinal = dfFinal.reset_index(drop=True)
dfFinal.to_csv('output3.csv',index=False)

# -------------------------- BAR GRAPH FIGURE
dfFinal = dfFinal.set_index('MatchesSplit')
plot = dfFinal.plot(kind='bar')
plot.set_ylabel("Counts")
plot.set_xlabel("Matches")

plot.bar_label(plot.containers[0])

plt.show()