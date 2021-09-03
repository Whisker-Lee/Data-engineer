import pandas as pd
import numpy as np

data = {
    'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
    'year':[2000,2001,2002,2001,2002],
    'pop':[1.5,1.7,3.6,2.4,2.9]
}

frame = pd.DataFrame(data)
print(frame)

frame2 = pd.DataFrame(data, index=['one','two','three','four','five'],columns=['year','state','pop','debt'])
print(frame2)
print(frame2.dtypes)
print(frame2.values)
print(type(frame2))
print(type(frame2['year']))


data = pd.DataFrame(np.arange(16).reshape((4,4)),index = ['Ohio','Colorado','Utah','New York'],columns=['one','two','three','four'])
print(data[['two','three']])
print(type(data[['two','three']]))
data[:2]
data[data['three']>5]
print(data.loc[['Ohio','Colorado'],['two','three']])
print(data.loc['Colorado',['two','three']])
print(data.iloc[0:3,2])
print(type(data.iloc[0:3,2]))
data['five'] = [1,2,3,4]
print(data)
val = pd.Series([-1.2,-1.5,-1.7],index=['Ohio','four','five'])
data['debt'] = val
print(data)



frame = pd.DataFrame(np.arange(9).reshape((3,3)),index=[1,4,5],columns=['Ohio','Texas','California'])
frame2 = frame.reindex([1,2,5,4])
print(frame2)

frame = pd.DataFrame(np.arange(9).reshape((3,3)),index = ['a','c','d'],columns = ['Ohio','Texas','California'])
frame2 = frame.drop(['a'])
frame2 = frame.drop('Ohio',axis=1)
print(frame2)
print(frame.index)
print(frame.iloc[0:2,0:2].index)


frame = pd.DataFrame(np.arange(8).reshape((2,4)),index=[3,2],columns=['d','a','b','c'])
print(frame.sort_index(1))
print(frame.sort_index(ascending=False))
print(frame.sort_index(1,ascending=False))
print(frame.sort_index(0,ascending=False))
frame2 = frame.sort_index()
print(frame2)
frame2.loc[2,'b']=1
print(frame2.sort_values(by=['a','b'],ascending = False))


data = pd.DataFrame([[1,6.5,np.nan],[1,np.nan,np.nan],[np.nan,np.nan,np.nan],[np.nan,6.5,np.nan]])
print(data)
print(data.dropna())
print(data.dropna(how='all',axis=1))


a = np.arange(25, dtype=float).reshape((5, 5))
print(len(a))
for i in range(len(a)):
    a[i, :i] = np.nan
a[0, 0] = np.nan
a[2, 0] = 0
df = pd.DataFrame(data=a, columns = list('ABCDE'))
print(df)
print(df.fillna(method='pad'))


frame = pd.DataFrame(np.arange(9).reshape((3,3)),index = ['a','c','d'],columns = ['Ohio','Texas','California'])
print(frame.corr())
frame['Ohio'] = frame['Ohio']**2
print(frame)
frame.loc['a','Ohio'] = np.nan
frame.loc['c','Ohio'] = np.nan
frame['r'] = frame['Ohio'].rank()
print(frame)
print(list(frame.index))
print(frame['Ohio'].unique())
print(type(frame['Ohio'].unique()))
print(frame['Ohio'].value_counts())
print(type(frame['Ohio'].value_counts()))
a = frame['Ohio'].value_counts()
print(pd.DataFrame(a))
print(a.index.values)
print(frame.index.values)
print(frame.columns.values)