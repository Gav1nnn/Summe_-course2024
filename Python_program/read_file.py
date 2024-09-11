# 逐行读取
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())
# 一次性读取
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
