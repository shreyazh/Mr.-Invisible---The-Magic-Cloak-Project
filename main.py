import numpy as n
import cv2

def shreyash(i):
    print()

cp = cv2.VideoCapture(0)
br = cv2.namedWindow("bars")

cv2.createTrackbar("upper_hue", "bars", 10, 180, shreyash)
cv2.createTrackbar("upper_saturation", "bars", 255, 255, shreyash)
cv2.createTrackbar("lower_hue", "bars", 0, 180, shreyash)
cv2.createTrackbar("upper_value", "bars", 255, 255, shreyash)
cv2.createTrackbar("lower_saturation", "bars", 150, 255, shreyash)
cv2.createTrackbar("lower_value", "bars", 50, 255, shreyash)


while True:
    cv2.waitKey(1000)
    ret, init_frame = cp.read()
    if ret:
        break

while True:
    ret, frame = cp.read()
    inspect = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    upper_hue = cv2.getTrackbarPos("upper_hue", "bars")
    upper_saturation = cv2.getTrackbarPos("upper_saturation", "bars")
    upper_value = cv2.getTrackbarPos("upper_value", "bars")
    lower_value = cv2.getTrackbarPos("lower_value", "bars")
    lower_hue = cv2.getTrackbarPos("lower_hue", "bars")
    lower_saturation = cv2.getTrackbarPos("lower_saturation", "bars")

    kernel = n.ones((3, 3), n.uint8)

    upper_hsv = n.array([upper_hue, upper_saturation, upper_value])
    lower_hsv = n.array([lower_hue, lower_saturation, lower_value])

    mask = cv2.inRange(inspect, lower_hsv, upper_hsv)
    mask = cv2.medianBlur(mask, 3)
    maskInv = 255 - mask
    mask = cv2.dilate(mask, kernel, 5)

    b = frame[:, :, 0]
    g = frame[:, :, 1]
    r = frame[:, :, 2]
    b = cv2.bitwise_and(maskInv, b)
    g = cv2.bitwise_and(maskInv, g)
    r = cv2.bitwise_and(maskInv, r)
    frameInv = cv2.merge((b, g, r))

    b = frame[:, :, 0]
    g = frame[:, :, 1]
    r = frame[:, :, 2]
    b = cv2.bitwise_and(b, mask)
    g = cv2.bitwise_and(g, mask)
    r = cv2.bitwise_and(r, mask)
    cloak_area = cv2.merge((b, g, r))

    final = cv2.bitwise_and(frameInv, cloak_area)

    cv2.imshow("Mr.Invisible's Power", final)
    cv2.imshow("original", frame)

    if cv2.waitKey(3) == ord("q"):
        break

cv2.destroyAllWindows()
cp.release()
