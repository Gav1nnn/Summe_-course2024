# 变量是存储数据的容器，如下我们定义个人信息
name = "Gavin" # 字符串类型
age = 20       # 整数类型
height = 1.83  # 浮点数类型
is_oucer = True# 布尔类型

print("Name:",name)
print("Age:",age)
print("Height:",height)
print("Is a student of OUC",is_oucer)

# python中运算符可以用于处理数学运算，字符串连接。
first="I am a"
second="student"
full=first+ " "+ second

print(full)

# 从用户那里获得输入，可以使用input()函数
user_name = input("what is your name?")

output = "Nice to meet you," + user_name +"!"
print(output)