import cv2
import numpy as np

image = cv2.imread("image.jpg")

alpha = 1.4
beta = 20
lofi = cv2.convertScaleAbs(image, alpha = alpha, beta = beta)

lofi = cv2.GaussianBlur(lofi, (3, 3), 0)

cv2.imwrite("modified_image.jpg", lofi)