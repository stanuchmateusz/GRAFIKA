import cv2
import numpy as np
import matplotlib.pyplot as plt


# image = cv2.imread('./img/salt-and-pepper-lena.jpg')
image = cv2.imread('./img/lenaRef.jpg', cv2.IMREAD_GRAYSCALE)
print(image.shape)
# przed
plt.figure(figsize=(11, 6))
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Original')
plt.xticks([]), plt.yticks([])
# po
image2 = image.copy()


plt.subplot(122), plt.imshow(image2,
                             cmap='gray'), plt.title('Wynik')
plt.xticks([]), plt.yticks([])
plt.show()
