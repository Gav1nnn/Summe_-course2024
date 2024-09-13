import torch

# 创建向量
vector1 = torch.tensor([1.0, 2.0, 3.0])
vector2 = torch.tensor([4.0, 5.0, 6.0])

# 向量加法
result_add = vector1 + vector2
print(f"向量加法结果: {result_add}")  # 输出: tensor([5., 7., 9.])

# 向量点积
result_dot = torch.dot(vector1, vector2)
print(f"向量点积结果: {result_dot.item()}")  # 输出: 32.0

# 向量的逐元素乘积
result_elementwise = vector1 * vector2
print(f"逐元素乘积结果: {result_elementwise}")  # 输出: tensor([ 4., 10., 18.])
