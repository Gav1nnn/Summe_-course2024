import torch

x = torch.tensor(2.0, requires_grad=True)

y = x**2 + 2*x + 1

# 计算梯度
y.backward()

# 输出梯度 (dy/dx)
print(f'The gradient of y with respect to x is: {x.grad.item()}')
