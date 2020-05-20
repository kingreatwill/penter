import cv2
import matplotlib.pyplot as plt

img = cv2.imread('../imagelib/lenna.jpg', 0)

# 灰度图显示，cmap(color map)设置为gray
plt.imshow(img, cmap='gray')
plt.show()

