import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import (binary_erosion, binary_dilation, binary_opening, binary_closing)
from skimage.color import rgb2hsv
from skimage.measure import label, regionprops

image = cv2.imread("task1.png")
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

_, d = cv2.threshold(image, 50, 255, 0)
_, d1 = cv2.threshold(image, 70, 255, 0)

areaz = []
numz = []
d = d - 255

eroded,eroded1 = label(binary_erosion(d)), label(binary_erosion(d1))

for i in range(2):
    d_1 = regionprops(eroded)[i].area
    areaz.append(d_1)
    numz.append(i+1)
for i in range(5):
    d1_1 = regionprops(eroded1)[i].area
    areaz.append(d1_1)
    numz.append(i+1)

d2_1 = regionprops(eroded1)[2].area
print(d2_1)

print(areaz)
print(numz)

num_areas = dict(zip(numz,areaz))
print(num_areas)
print(f"Наибольшая площадь: {max(num_areas, key=num_areas.get)}")

plt.subplot(121)
plt.imshow(eroded)
plt.subplot(122)
plt.imshow(eroded1)

plt.show()