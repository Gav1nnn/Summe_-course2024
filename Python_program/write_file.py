# 将一些文本写入到 'example.txt' 文件中
# 输出内容将覆盖已有文件内容
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a new file.\n")

# 将一些文本追加到 'example.txt' 文件末尾
with open('example.txt', 'a') as file:
    file.write("Appending a new line.\n")