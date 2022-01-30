import cv2
import numpy as np

# source: https://stackoverflow.com/questions/39752235/python-how-to-detect-vertical-and-horizontal-lines-in-an-image-with-houghlines-w

img = cv2.imread('../docs/Beispiele/Run 9/00.0-08.0-35.0-35.0-40.0-30.0-01.0-04.0-02.0-NONE.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
lines = cv2.HoughLinesP(image=edges, rho=1, theta=np.pi / 180, threshold=100, lines=np.array([]), minLineLength=150,
                        maxLineGap=3)

a, b, c = lines.shape
for i in range(a):
    cv2.line(img, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 2, cv2.LINE_AA)
    # cv2.imwrite('test.jpg', img)

cv2.imshow('img', img)
cv2.waitKey(0)
# cv2.destroyAllWindows()

# for r, theta in lines[0]:
#      a = np.cos(theta)
#     b = np.sin(theta)
#
#     x0 = a*r
#     y0 = b*r
#
#     x1 = int(x0 + 1000*(-b))
#     y1 = int(y0 + 1000 * a)
#
#     x2 = int(x0 - 1000 * (-b))
#     y2 = int(x0 - 1000 * a)
#
#     cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
#
# cv2.imwrite('test.jpg', img)
#
# img = cv2.imread('test.jpg')
# cv2.imshow('Line detection result', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# exit(0)
