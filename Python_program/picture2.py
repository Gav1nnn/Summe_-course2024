import cv2
import matplotlib.pyplot

# 读取图像
image = cv2.imread('ouc.png')

# 将图像转换为 RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 应用高斯模糊
blurred_image = cv2.GaussianBlur(image_rgb, (15, 15), 0)

# 显示模糊处理后的图像
matplotlib.pyplot.imshow(blurred_image)
matplotlib.pyplot.axis('off')
matplotlib.pyplot.show()


