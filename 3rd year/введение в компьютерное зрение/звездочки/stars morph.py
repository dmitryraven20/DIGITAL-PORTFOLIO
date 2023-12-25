import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import (binary_erosion, binary_dilation, binary_opening, binary_closing)

from skimage.measure import label

struct = np.ones((3,3))
starr = np.load(r"C:\\study\\stars.npy")
starr1 = binary_dilation(starr,struct)
labeled = label(starr)
plt.subplot(121)
plt.imshow(starr)

for lb in range(1, np.min(labeled)+1):
    new_image = np.zeros_like(starr1)
    new_image[labeled==lb] = 1
    print(lb)
    
plt.subplot(122)
plt.imshow(labeled)

print("Общее кол-во:", np.max(label(starr)))
print("Кол-во с вычетом эрозии:", np.max(label(starr)) - np.max(label(binary_erosion(starr, struct))))

plt.show()