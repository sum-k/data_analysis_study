
# Q1
def is_odd(a):
    if a % 2 == 0:
        return("짝수")
    else:
        return("홀수")

is_odd(3)

is_odd = lambda a: True if a % 2 == 0 eles False
is_odd(3)

# Q2
def avg_all(*args):
    sum = 0
    for i in args:
        sum += i
    avg = sum/len(args)
    return(avg)

avg_all(1,2,3,4,5)

# Q3
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다" % total)

# Q4
# 3. print("you", "need", "python")
# 문자열 사이에 공백이 추가된다.

# Q5
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()

with open("test.txt", 'w') as f1:
    f1.write("Life is too short! ")
with open("test.txt", 'r') as f2:
    print(f2.read())

# Q6
f = open("test.txt", 'a')
f.write(input("저장할 내용을 입력하세요:"))
f.write("\n")
f.close()
    
# Q7
f = open("test.txt", 'r')
body = f.read()
f.close()

new_body = body.replace("java", "python")

f = open("test.txt", 'w')
f.write(new_body)
f.close()