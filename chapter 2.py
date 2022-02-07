###  2-1. 숫자형
##### 사칙연산
a = 3
b = 4
a + b
a - b
a * b
a / b

##### 제곱
a ** b

##### 나눗셈 - 나머지, 몫
a % b
a // b

###  2-2. 문자열 자료형
##### 백슬래시 - 따옴표 중복사용 가능 
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."

#### 여러 줄 문자열
##### 이스케이프 코드 (\n, \t :탭 간격, \\, \', \")
multiline = "Life is too short\nYou need python" 
multiline='''
Life is too short
You need python
'''
print(multiline)

##### 문자열 연산
head = "Python"
tail = " is fun!"
head + tail
head * 2

##### 문자열 길이 구하기
a = "Life is too short"
len(a)

##### 문자열 인덱싱 - 파이썬은 0부터 시작!
a = "Life is too short, You need Python"
a[3]
a[-1] #뒤에서부터 첫번째(n)
a[-0] #(=a[0])

##### 문자열 슬라이싱
a = "Life is too short, You need Python"
a[0:4] #끝번호는 포함하지 않음 (0 <= a < 4)
a[19:] #끝까지
a[:17] #처음부터
a[:] #전체

##### 문자열 포매팅(포맷 코드 사용)
"I eat %d apples." % 3 # %d(숫자 - 정수)
"I eat %s apples." % "five" # %s(문자열, 소수를 넣으면 문자열로 인식!)
number = 3
"I eat %d apples." % number

number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % (number, day)

"Error is %d%%." % 98 #문자 % 가 필요할 때

##### 포맷 코드 + 숫자
"%10s" % "hi" #대입되는 값을 오른쪽 정렬, 나머지는 공백
"%-10sjane." % 'hi' #대입되는 값 왼쪽 정렬, 나머지는 공백
"%0.4f" % 3.42134234 #소숫점 네 번째 자리까지 나타내기
"%10.4f" % 3.42134234 #오른 쪽 정렬 ~

##### 문자열 포매팅(format 함수 사용)
"I eat {0} apples".format(3)
"I eat {0} apples".format("five")
number = 3
"I eat {0} apples".format(number)

number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days.".format(number, day) #0과 1은 순서를 의미
"I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3) #인덱스와 이름 혼용도 가능

##### 정렬(왼쪽, 오른쪽, 가운데)
"{0:<10}".format("hi") #문자열의 총 자릿수는 10
"{0:>10}".format("hi")
"{0:^10}".format("hi")
##### 공백 채우기
"{0:=^10}".format("hi")
"{0:!<10}".format("hi")

y = 3.42134234
"{0:0.4f}".format(y)
"{{ and }}".format() #문자 그대로 표현하기

##### f 문자열 포매팅
name = '홍길동'
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
f'나는 내년이면 {age+1}살이 된다.'

d = {'name':'홍길동', 'age':30} #딕셔너리
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'

f'{"hi":<10}
f'{"hi":>10}'
f'{"hi":^10}'
f'{"hi":=^10}'
f'{y:0.4f}'
f'{{ and }}'

##### 문자열 관련 함수
a = "Python is the best choice"
a.count('i') #문자 개수 세기

a.find('b') #위치 알려주기1 / 존재하지 않는 문자에 '-1' 반환
a.index('t') #위치 알려주기2 / 존재하지 않는 문자에 오류 반환

",".join('abcd') #문자열 삽입
",".join(['a', 'b', 'c', 'd'])

a = 'hi'
a.upper() #소문자 -> 대문자
a.lower() #대문자 -> 소문자

a = " hi "
a.lstrip() #왼쪽 공백 지우기
a.rstrip() #오른쪽 공백 지우기
a.strip() #양쪽 공백 지우기

a = "Life is too short"
a.replace("Life", "Your leg") #문자열 바꾸기

a.split() #문자열 나누기(공백 기준) -> 리스트로 반환
b = "a:b:c:d"
b.split(':')

###  2-3. 리스트 자료형
##### 리스트 인덱싱, 슬라이싱
a = [1, 2, 3, ['a', 'b', 'c']]
a[3]
a[-1][0]
a[-1][:2]

##### 연산과 반복(*) 가능
a = [1, 2, 3]
a[2] + "hi" #연산 오류 발생
str(a[2]) + "hi" #오류 해결

##### 리스트 수정과 삭제
a = [1, 2, 3]
a[2] = 4

del a[1]

##### 리스트 관련 함수들
a = [1, 2, 3]
a.append(4) #리스트에 요소 추가
a.append([5,6]) #자료형(리스트) 추가도 가능 
a

a = [1, 4, 3, 2]
a.sort() #리스트 정렬
a

a = ['a', 'c', 'b']
a.reverse() #뒤집기(거꾸로)

a.index('a') #위치 반환/ 존재하지 않으면 오류 발생

a.insert(0, 4) #리스트에 요소 삽입(0번째에 4를 삽입)

a = [1, 2, 3, 1, 2, 3]
a.remove(3) #첫 번째로 나오는 3을 제거

a.pop() #맨 마지막 요소 반환, 삭제
a.pop(1) # 1번째 요소 반환, 삭제

a.count(1) #요소의 개수세기

a = [1,2,3]
a.extend([4,5]) #리스트 확장/ 리스트만 올 수 있다

###  2-4. 튜플 자료형
t2 = (1,) #1개의 요소일 때 반드시 콤마
t3 = (1, 2, 3)
t4 = 1, 2, 3 #괄호 생략가능

###### 요소값 삭제와 변경이 불가능하다.
###### 인덱싱과 슬라이싱 가능
###### 튜플 더하기, 곱하기 가능
###### len() 함수로 길이 구하기 가능

###  2-5. 딕셔너리 자료형
a = {1: 'hi'} 
a = { 'a': [1,2,3]}

##### 딕셔너리 쌍 추가하기
a = {1: 'a'}
a[2] = 'b'
a
a[3] = [1,2,3]
a

##### 딕셔너리 요소 삭제하기
del a[1] #해당 key에 맞는 쌍이 삭제됨

##### key 사용 value 얻기
grade = {'pey': 10, 'julliet': 99}
grade['pey']

###### 동일한 key가 존재하면 하나를 제외한 나머지 것들이 모두 무시된다.
###### key에는 리스트를 쓸 수 없다.

##### 딕셔너리 관련 함수들
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
a.keys() #key 리스트 만들기/ append, insert, pop 등 함수 수행은 불가
for k in a.keys():
    print(k)

a.values() #value 리스트 만들기

a.items() #key, value 쌍 얻기

a.clear() #쌍 모두 지우기

a.get('name') #key 사용 value 얻기
print(a.get('nokey')) #none 반환
print(a['nokey']) #오류 발생
a.get('foo', 'bar') #'foo'가 존재하지 않으면 'bar'(디폴트 값) 반환

'name' in a #조사하기 (True/False)

###  2-6. 집합 자료형
s1 = set([1,2,3])
s2 = set("Hello")

###### 중복허용하지 않음(필터 역할)
###### 순서가 없음 -> 인덱싱 불가 -> 리스트 or 튜플로 변환

l1 = list(s1)
l1[0]

t1 = tuple(s1)
t1[0]

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
##### 교집합
s1 & s2
s1.intersection(s2)
##### 합집합 
s1 | s2
s1.union(s2)
##### 차집합
s1 - s2
s1.difference(s2)

##### 집합 자료형 관련 함수들
s1 = set([1, 2, 3])
s1.add(4) #값 1개 추가하기

s1.update([5,6]) #값 여러 개 추가하기

s1.remove(2) #특정 값 제거하기



