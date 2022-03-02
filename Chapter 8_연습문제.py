# 연습문제

# Q1. 문자열 바꾸기
a = "a:b:c:d"
"#".join(a.split(":"))

# Q2. 딕셔너리 값 추출하기
a = {'A':90, 'B':80}
a.get('C', 70)

# Q3. 리스트 더하기와 extend 함수
a = [1, 2, 3]
id(a)
a = a + [4,5]
id(a)

a = [1, 2, 3]
id(a)
a.extend([4, 5])
id(a)
# extend를 사용하여 더한 경우 주소 값이 변하지 않고 그대로 유지된다.

# Q4. 리스트 총합 구하기
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0
for i in A:
    if i >= 50:
        sum += i

print(sum)

### Q5. 피보나치 함수
def fibo(n):
    if n == 0:
        return 0
    if n == 1: 
        return 1
    return fibo(n-2) + fibo(n-1)

for i in range(10):
    print(fibo(i))

# Q6. 숫자의 총합 구하기
# def sum(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result

# sum(65,45,2,3,45,8)

num = input("숫자를 입력하세요: ")
numbers = num.split(",")
total = 0
for n in numbers:
    total += int(n)
print(total)


# Q7. 한 줄 구구단
num = int(input("구구단을 출력할 숫자를 입력하세요(2~9):"))
for i in range(1, 10):
    print(i*num, end =" ")

### Q8. 역순 저장
f = open("abc.txt", 'r')
lines = f.readlines()
f.close()

lines.reverse()

f = open('abc.txt', 'w')
for i in lines:
    line = i.strip()
    f.write(line)
    f.write('\n')
f.close()

# Q9. 평균값 구하기
f = open("abc.txt", 'r')
lines = f.readlines()
f.close()

sum = 0
for num in lines:
    sum += int(num)

avg = sum/len(lines)

f2 = open("result.txt", "w")
f2.write(str(avg))
f2.close()

# Q10. 사칙연산 계산기
class Calculator:
    def __init__(self, num):
        self.numlist = num
    def sum(self):
        result = 0
        for i in self.numlist:
            result += i
        return result
    def avg(self):
        sum = self.sum()
        return sum/len(self.numlist)

cal1 = Calculator([1,2,3,4,5])
cal1.sum()
cal1.avg()

cal2 = Calculator([6,7,8,9,10])
cal2.sum()
cal2.avg()

### Q11. 모듈 사용 방법
# import mymod

#1. sys모듈 사용
import sys
sys.path.append("C:/doit")
import mymod

#2. PYTHONPATH 환경 변수 사용
#3. 현재 디렉터리 사용

# Q12. 오류와 예외 처리
result = 0

try:
    [1, 2, 3][3]
    "a"+1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3
finally:
    result += 4

print(result)

# 7
# 처음에 indexerror 발생, finally는 무조건 실행

### Q13. DashInsert 함수
data = "4546793"
numbers = list(map(int, data))   # 숫자 문자열을 숫자 리스트로 변경
result = []

for i, num in enumerate(numbers):
    result.append(str(num))
    if i < len(numbers)-1:                   # 다음 수가 있다면
        is_odd = num % 2 == 1                # 현재 수가 홀수
        is_next_odd = numbers[i+1] % 2 == 1  # 다음 수가 홀수
        if is_odd and is_next_odd:           # 연속 홀수
            result.append("-")
        elif not is_odd and not is_next_odd: # 연속 짝수
            result.append("*")

print("".join(result))

# Q14. 문자열 압축하기
def compress_string(s):
    _c = ""
    cnt = 0
    result = ""
    for c in s:
        if c!=_c:
            _c = c
            if cnt: result += str(cnt)
            result += c
            cnt = 1
        else:
            cnt +=1
    if cnt: result += str(cnt)
    return result

print(compress_string("aaabbcccccca"))

# Q15. Duplicate Numbers
def chkDupNum(s):
    result = []
    for num in s:
        if num not in result:
            result.append(num)
        else:
            return False
    return len(result) == 10

print(chkDupNum("0123456789"))      
print(chkDupNum("01234"))          
print(chkDupNum("01234567890"))    
print(chkDupNum("6789012345"))  
print(chkDupNum("012322456789")) 

# Q16. 모스 부호 해독
dic = {
    '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z'
}

def morse(src):
    result = []
    for word in src.split("  "):
        for char in word.split(" "):
            result.append(dic[char])
        result.append(" ")
    return "".join(result)


print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))

# Q17. 기초 메타 문자
# 2 / [.]:문자 그대로 ".", 3번이상 반복을 의미

# Q18. 문자열 검색
import re
p = re.compile("[a-z]+")
m = p.search("5 python")
m.start() + m.end()
# 2 + 8 = 10

# Q19. 그루핑
import re
a = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""
pat = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
print(pat.sub("\g<1>-####", a))

# Q20. 전방 탐색
import re

pat = re.compile(".*[@].*[.](?=com$|net$).*$")

print(pat.match("pahkey@gmail.com"))
print(pat.match("kim@daum.net"))
print(pat.match("lee@myhome.co.kr"))


