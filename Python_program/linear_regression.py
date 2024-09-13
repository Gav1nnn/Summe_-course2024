import torch
import torch.nn as nn
import torch.optim as optim

# 生成一些简单的数据
x_train = torch.tensor([[1.0], [2.0], [3.0]], dtype=torch.float32)
y_train = torch.tensor([[2.0], [4.0], [6.0]], dtype=torch.float32)

# 定义线性模型
model = nn.Linear(1, 1)

criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

for epoch in range(100):
    model.train()
    
    y_pred = model(x_train)
    loss = criterion(y_pred, y_train)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if epoch % 10 == 0:
        print(f'Epoch [{epoch+1}/100], Loss: {loss.item():.4f}')

# 测试模型
model.eval()
with torch.no_grad():
    test_input = torch.tensor([[4.0]], dtype=torch.float32)
    prediction = model(test_input)
    print(f"\nInput: 4.0, Predicted Output: {prediction.item():.4f}")
