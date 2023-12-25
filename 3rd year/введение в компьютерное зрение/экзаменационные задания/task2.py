import cv2
import matplotlib.pyplot as plt
from skimage.color import rgb2hsv
from skimage.measure import label, regionprops

image = cv2.imread("task2.png")
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h1 = hsv[:, :, 1]

ret, h1 = cv2.threshold(h1, 254, 255, 200)

result = cv2.bitwise_and(image, image, mask=h1)

plt.subplot(121)
plt.imshow(image)
plt.subplot(122)
plt.imshow(result)

plt.show()