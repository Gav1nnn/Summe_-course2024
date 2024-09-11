# 列表
codes_list = ["C++", "Python", "Java"]
# 添加新项目
codes_list.append("Go")
print(codes_list)  
# 删除一个项目
codes_list.remove("C++")
print(codes_list)  
# 访问列表中的元素
first_item = codes_list[0]
print(first_item)  
# 列表切片
sub_list = codes_list[1:]
print(sub_list)  

# 元组
# 创建一个坐标点的元组
coordinate = (10, 20)
# 访问元组中的元素
x, y = coordinate
print(f"x: {x}, y: {y}")

# 字典
# 创建一个学生成绩的字典
grades = {"A": 85, "B": 90, "C": 78}

# 添加或更新一个学生的成绩
grades["D"] = 92
grades["A"] = 88
print(grades)

# 访问一个学生的成绩
print(grades["B"])

# 删除一个学生的成绩
del grades["C"]
print(grades)  
# 检查某个学生是否在字典中
if "Eve" in grades:
    print("E's grade:", grades["E"])
else:
    print("E is not in the grades list.")  # 输出: Eve is not in the grades list.

# 集合
# 创建一个集合
fruits = {"apple", "banana", "cherry", "apple", "banana"}

# 去掉重复的
print(fruits)

# 添加新元素
fruits.add("orange")
print(fruits)

# 计算两个集合的交集和并集
set_a = {"apple", "banana", "cherry"}
set_b = {"banana", "orange", "grape"}

intersection = set_a & set_b  # 交集
union = set_a | set_b  # 并集

print("Intersection:", intersection) 
print("Union:", union) 
