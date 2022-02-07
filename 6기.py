import pandas as pd
import numpy as np

#1
a=[0, 2, 4, 6, 8]
b=[1, 3, 5, 7, 9]
print(a,b)

#2
a = 10
b = (1.44,'bitamin')
c = "비타민"
d = [1, 2, 3, 4, 5]
e = {'특별시':'천안','충남':'서울','인천':'광역시'} 

type(a)
type(b)
type(c)
type(d)
type(e)

#3
score = [90,25,67,45,80]
for i in score:
    if i >= 80:
        print("우수")
    elif i >= 60:
        print("보통")
    else:
        print("미흡")

#4
import seaborn as sns  
titanic=sns.load_dataset('titanic')
titanic.head(3)

#4-1
df = titanic.loc[:,['pclass','fare']]
df.head(3)

#4-2
def z_score(df_input):
    return df_input.apply(lambda x: (x-min(x)) / (max(x)-min(x)))

#4-3
print(z_score(df)['fare'])

#5 
df = pd.read_csv('insurance2.csv')
df.isnull().sum()
df.fillna(method='ffill', inplace=True)