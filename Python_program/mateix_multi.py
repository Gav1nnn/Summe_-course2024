import torch

# 创建两个矩阵
A = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
B = torch.tensor([[5.0, 6.0], [7.0, 8.0]])

# 矩阵乘法
C = torch.matmul(A, B)
print("Matrix Multiplication Result:\n", C)
