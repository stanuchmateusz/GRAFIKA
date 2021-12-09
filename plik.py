import cv2
import numpy as np
import matplotlib.pyplot as plt


# gray_img = cv2.imread('./original.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('./original.jpg')
print(type(img))
print(img.shape)


# c = 1.0
c = 0.5
b = 50
# img = c*img - b


# for i in range(0, img.shape[0]):     to jest to samo co img = c*img -b
#     for j in range(0, img.shape[1]):
#         img[i, j] = c*img[i, j]+b


cv2.imshow("obraz", img)

# cv2.waitKey()
# tab = np.ndarray(img.shape, dtype="uint8")
# print(tab.shape)
# print(tab)
# cv2.imshow("obraz2", tab)
# cv2.waitKey()


# HISTOGRAMMMM


# plt.subplot(3, 1, 1)
# plt.hist(img[0].ravel(), 256, [0, 256])
# # plt.waitforbuttonpress()

# plt.subplot(3, 1, 2)
# plt.hist(img[1].ravel(), 256, [0, 256])
# # plt.waitforbuttonpress()

# plt.subplot(3, 1, 3)
# plt.hist(img[2].ravel(), 256, [0, 256])
# plt.xlabel("kolory")

# plt.waitforbuttonpress()
cv2.destroyAllWindows()
