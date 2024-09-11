# 条件判断if-elif-else，判断时可以使用and或or来进行
age = 20
is_student = False

if age >= 18 and is_student:
    print("You are an adult student.")
elif age >= 18 and not is_student:
    print("You are an adult, but not a student.")
else:
    print("You are not an adult.")

# 循环(for while)
codes = ["Java","C++","Python"]
for code in codes:
    print(code)

count = 0
while count < 5:
    print(count)
    count += 1

# break、continue 和 pass
numbers = [3, 0, 5, 8, 7, 2, 10, 0, 9]

for number in numbers:
    if number == 0:
        pass  # 0 是特殊情况，这里什么也不做，继续处理下一个数字
    elif number % 2 != 0:
        continue  # 奇数情况下跳过处理
    elif number == 7:
        print("Found 7, stopping the loop.")
        break  # 遇到 7 时停止循环
    print(f"Processing number: {number}")

print("Loop ended.")

