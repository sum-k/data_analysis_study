
#1
중간고사 = [34, 30, 26, 40, 33, 15, 31, 21, 17, 40]
기말고사 = [45, 48, 25, 50, 50, 28, 39, 33, 47, 42]
과제 = [5, 10, 8, 10, 10, 7, 7, 9, 10, 2]

총점 = []
for i, j, k in zip(중간고사, 기말고사, 과제):
    총점.append(i + j + k)

총점.sort(reverse=True)
print(총점)

#2
sn = input('지원번호를 입력하세요: ')

if sn[3] == '1' or sn[3] == '3':
    print('성별: 남')
else:
    print("성별: 여")
if sn[3]== '1' or sn[3] == '2' :
    print('기수: ',((2000+int(sn[:2])) -2018)*2 + int(sn[2]))
    print('편입: x ' )
else :
    print('기수: ',((2000+int(sn[:2])) -2018)*2 + int(sn[2])-1)
    print('편입: o')
if sn[-1] == 's' :
    print('운영진: o ')
else :
    print('운영진: x ')

#3
import pandas as pd
import numpy as np

#3-1
titanic=sns.load_dataset('titanic')
titanic

#3-2
df = titanic.loc[:100, ['pclass', 'age', 'fare']]
df.head()

#3-3
df.drop('pclass', axis = 1, inplace=True)
df

#3-4
df.isnull().sum()

#3-5
df.bfill(inplace=True)

#3-6
df.query('age >= 40').sort_values(by='age', ascending=False)

#3-7
mean = df.fare.mean()
std = df.fare.std()
df.fare.apply(lambda x : (x-mean)/std)

#3-8
titanic['first_name']=titanic.name.apply(lambda x : x.split(',')[0])
titanic


