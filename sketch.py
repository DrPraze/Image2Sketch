import cv2
gray = cv2.cvtColor(cv2.imread('test.jpg'), cv2.COLOR_BGR2GRAY)
smoothing = cv2.GaussianBlur(cv2.bitwise_not(gray), (21, 21), sigmaX = 0, sigmaY = 0)
image = cv2.divide(gray, 255 - smoothing, scale = 256)
cv2.imshow("image", image)
cv2.waitKey()
