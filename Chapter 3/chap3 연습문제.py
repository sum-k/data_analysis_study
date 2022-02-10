# Q1
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

#shirt

# Q2
result = 0
a = 1

while a <= 1000:
    a += 1
    if a % 3 == 0:
        result += a
    
print(result)
     
# Q3
a = 0
while a < 5:
    a += 1
    print("*"*a)

# Q4
for i in range(1, 101):
    print(i)

# Q5
exam = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for score in exam:
    sum += score

print(sum/len(exam)) 

# Q6
# numbers = [1, 2, 3, 4, 5]
# result = []
# for n in numbers:
#     if n % 2 == 1:
#         result.append(n*2)

numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n % 2 == 1]
print(result)