import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label, regionprops

x, y, xy, yx = [], [], [], []

for i in range(100):
    image = np.load(f"out/h_{i}.npy")
    labeled = label(image)
    regions = sorted(regionprops(labeled), key=lambda region: region.area)

    (x_1, y_1),(x_2, y_2) = regions[1].centroid,regions[0].centroid
    
    x.append(x_1)
    y.append(y_1)

    yx.append(x_2)
    xy.append(y_2)

plt.plot(x, y)
plt.plot(xy, yx)
plt.show()