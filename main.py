import numpy as np
from matplotlib import pyplot as plt, image


# x = np.arange(0,6, 0.1)
# y = np.sin(x)

# plt.plot(x, y)
# plt.show()

img = image.imread('./images/pepetest.jpg')

plt.imshow(img)
plt.show()
