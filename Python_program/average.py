# 计算列表中数字的平均值
def calculate_average(numbers):
    if not numbers:  # 检查列表是否为空
        return 0
    total = sum(numbers)  # 计算所有数字的和
    count = len(numbers)  # 计算列表中数字的个数
    average = total / count  # 计算平均值
    return average

# 数据
numbers = [100,100,300]

# 调用函数并打印结果
average = calculate_average(numbers)
print(f"The average of the list is: {average}")
