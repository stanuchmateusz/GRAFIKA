import cv2
import numpy as np
import matplotlib.pyplot as plt


img_1 = cv2.imread('./rudzia.png')
img_3 = cv2.imread('./rudzia2.png')

print(img_1.shape)
print(img_3.shape)

# img_3 = img_2[0:512, 0:512, :]  # obcinanie zdjęcia, wytnie 512 na 512, 3 wymiar to nie wiem
# cv2.imshow("grzyb", img_3)

a = 1
img_4 = a * img_1
cv2.imshow("grzyb", img_4)

cv2.waitKey()

cv2.destroyAllWindows()
