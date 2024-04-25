"""Esimerkki binäärisestä EI-operaatiosta"""

import cv2
import numpy as np

# Kuva ja sen negaatio
kuva1 = cv2.imread("03-laskutoimitukset/seamk_logo.jpg", 0)
kuva2 = cv2.bitwise_not(kuva1)

# Kuvat vierekkäin ja pienemmäksi
kuvat = np.hstack((kuva1, kuva2))
kuvat = cv2.resize(kuvat, None, fx=0.5, fy=0.5)
#cv2.imwrite("kuvituskuvat/bitwise_not.jpg", kuvat)

cv2.imshow("kuvat", kuvat)
cv2.waitKey(0)