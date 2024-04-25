"""Esimerkki värien etsinnästä HSV-värimallin avulla"""

import cv2
import numpy as np

kuva = cv2.imread("05-varit/pallot.jpg")
kuva_hsv = cv2.cvtColor(kuva, cv2.COLOR_BGR2HSV)

alaraja = (85, 50, 50)
ylaraja = (130, 255, 255)

maski = cv2.inRange(kuva_hsv, alaraja, ylaraja)
maskattu = cv2.bitwise_and(kuva, kuva, mask=maski)

kuvat = np.hstack((cv2.cvtColor(maski, cv2.COLOR_GRAY2BGR), maskattu))

cv2.imwrite("kuvituskuvat/pallot_hsv_sininen.jpg", kuvat)
cv2.imshow("maski ja maskaus", kuvat)
cv2.waitKey(0)