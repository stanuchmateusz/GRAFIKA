import cv2
import numpy as np
import matplotlib.pyplot as plt


# image = cv2.imread('./img/salt-and-pepper-lena.jpg')
# image = cv2.imread('./img/lenaRef.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.imread('./img/rudzia.png', cv2.IMREAD_GRAYSCALE)
print(image.shape)
# przed
plt.figure(figsize=(11, 6))
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Original')
plt.xticks([]), plt.yticks([])
# po
ksize = 9
# image2 = image.copy()
image2 = cv2.blur(image, (ksize, ksize))  # to jest filtracja ugułem


a = 255  # próg górny
b = 60  # próg dolny
for i in range(0, image2.shape[0]):
    for j in range(0, image2.shape[1]):
        image2[i][j] = 255 if image2[i][j] < a and image2[i][j] > b else 0

plt.subplot(122), plt.imshow(image2,
                             cmap='gray'), plt.title('Wynik')
plt.xticks([]), plt.yticks([])
plt.show()
