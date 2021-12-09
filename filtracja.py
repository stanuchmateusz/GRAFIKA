import cv2
import numpy as np
import matplotlib.pyplot as plt


# image = cv2.imread('./img/salt-and-pepper-lena.jpg')
image = cv2.imread('./img/lenaRef.jpg')
print(image.shape)

plt.figure(figsize=(12, 6))
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Original')
plt.xticks([]), plt.yticks([])

ksize = 9
# jest też zywkły cv2.blur(image,(ksise,ksize))
new_image_gauss = cv2.GaussianBlur(image, (ksize, ksize), 0)

plt.subplot(122), plt.imshow(new_image_gauss,
                             cmap='gray'), plt.title('Gaussian Filter')
plt.xticks([]), plt.yticks([])

plt.show()
# cv2.imshow("Rudzia", img)

# cv2.waitKey()

# cv2.destroyAllWindows()
