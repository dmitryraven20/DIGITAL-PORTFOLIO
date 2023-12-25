import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import (binary_erosion, binary_dilation, binary_opening, binary_closing)

from skimage.measure import label

wires = np.load(r"C:\\study\\wires6.npy")
struct = np.ones((3,1))
labeled = label(wires)
plt.subplot(121)
plt.imshow(labeled)

for lb in range(1, np.max(labeled)+1):
    new_image = np.zeros_like(wires)
    new_image[labeled==lb] = 1
    wir1 = label(binary_erosion(new_image,struct))
    t = np.max(wir1)
    if t == 1:
        print("Провод №", lb, "Провод цел")
    elif t < 1:
        print("Провод №", lb, "Провод изношен")
    else:
        print("Провод №", lb, "Частей:", t, "Разрывов:", t-1)
# print(wires)

wires1 = binary_erosion(wires, struct)
# print(wires1)


plt.subplot(122)
plt.imshow(binary_erosion(wires, struct))
plt.show()
