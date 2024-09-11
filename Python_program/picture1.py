import cv2         # OpenCV库，用于图像处理
import matplotlib.pyplot  # Matplotlib库，用于图像显示

# 1. 读取图像
image = cv2.imread('ouc.png')
# 2. 转换为灰度图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 3. 显示原图像和灰度图像
matplotlib.pyplot.subplot(1, 2, 1)  # 创建一个 1x2 的子图布局，当前选择第 1 个子图
matplotlib.pyplot.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # 转换并显示原图像
matplotlib.pyplot.title('Original Image')  # 设置子图的标题

matplotlib.pyplot.subplot(1, 2, 2)  # 选择第 2 个子图
matplotlib.pyplot.imshow(gray_image, cmap='gray')  # 直接显示灰度图像（不需要转换）
matplotlib.pyplot.title('Gray Image')  # 设置子图的标题

matplotlib.pyplot.show()  # 显示图像窗口
