# Q1.
(80 + 75 + 55)/3

# Q2.
13 % 2 

# Q3. 
id = '881120-1068234'
'19'+id[:6] #생년월일
id[7:]

# Q4.
pin = "881120-1068234"
pin[0]

# Q5.
a = "a:b:c:d"
a.replace(":","#")

# Q6.
l1 = [1, 3, 5, 4, 2]
l1.sort()
l1.reverse()
l1

# Q7.
' '.join(['Life', 'is', 'too', 'short'])

# Q8.
t1 = (1,2,3)
t1 + (4,)

# Q9.
#2번/ key값이 튜플이라서? 

# Q10.
a = {'A':90, 'B':80, 'C':70}
a.pop('B')

# Q11.
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
set(a)

# Q12.
a = b = [1, 2, 3]
a[1] = 4
print(b)
#같이 수정된다. 주소값이 같게 설정되기 때문에

mystr = "13"
"{0:0>5}".format(mystr)


#마민경
# 1.
a = 30
b = 17
a // b
a % b

# 2.
x = "world Hello"
f = x[:5]
s = x[6:]
s + ' ' + f

# 3.
a = "That's pretty good Idea"
a.upper()

# 4.
h = "Hi"
print(h * len(h))

# 5.
site = 'http://naver.com'
new_site = site[7:]
indx = new_site.index('.')
new_site_2 = new_site[:indx]
password = new_site_2[:3] + str(len(new_site_2)) + str(new_site_2.count('e')) + '!'

print("{0}의 비밀번호는 {1} 입니다.".format(site, password))

#박민영

# 1.
multiline = '''
안녕하세요.
저는    박민영   입니다.
'''
print(multiline)

# 2.
dic = {'메로나':1000, '폴라포':500, '빵빠레':1100}
dic['죠스바'] = 400
dic['월드콘'] = 900
dic

# 3.
inventory = {'메로나':[1000, 15], '폴라포':[500, 20], '빵빠레':[1100, 10]}
inventory['메로나'][0]

# 4.
study = {'강수민':15, '구남이':16, '마민경':17, '박민영':19}
list(study.keys())
list(study.values())
list(study.items())

# 5.
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)

# 6.
"Profit from export roses {}%".format(7.3)

# 7.
안녕 = "안-녕-하-십-니-까-만-나-서-반-갑-습-니-다-앞-으-로-스-터-디-열-심-히-해-봅-시-다-화-이-팅-입-니-다"
print(안녕)

#구남이 

# 1.
movie_rank = ['닥터 스트레인지', '스플릿', '럭키']

# 2.
movie_rank.append('배트맨')
movie_rank

#3.
movie_rank.insert(1, '슈퍼맨')
movie_rank

#4.
movie_rank.remove('럭키')

#5.
t1 = (1,)
type(t1)

#6.
#튜플엔 추가나 삭제 등 편집이 불가능하다.

#강수민

#1.
close_price_daeshin = [10000, 10500, 10300, 10700, 11100]
average= sum(close_price_daeshin)/len(close_price_daeshin)

print("average: " + str(average))

#2.
nums = [1, 2, 3, 4, 5]
nums.remove(4)
nums.remove(5)
nums

#3.
items = ['000600', '034560', '003540', '039490']
';'.join(items)

#4.
mystr = '13'
"{0:0>5}".format(mystr)

#5.
a = {'A':90, 'B':80}
a.get('C', 70)