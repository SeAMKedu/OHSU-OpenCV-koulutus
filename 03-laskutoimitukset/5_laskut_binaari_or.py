"""Esimerkki binäärisestä TAI-operaatiosta"""

import cv2
import numpy as np

kuva1 = cv2.imread("03-laskutoimitukset/seamk_logo.jpg", 0)
kuva2 = cv2.imread("03-laskutoimitukset/opencv_logot.jpg", 0)

# Pikselittäinen tai-operaatio kuville
kuva3 = cv2.bitwise_or(kuva1, kuva2)

# Määritellään kuvien korkuinen pystysuora musta palkki
marginaali = np.ones((kuva1.shape[0], 10), dtype="uint8")*255

# Kuvat vierekkäin ja palkki väliin
kuvat = np.hstack((kuva1, marginaali))
kuvat = np.hstack((kuvat, kuva2))
kuvat = np.hstack((kuvat, marginaali))
kuvat = np.hstack((kuvat, kuva3))

kuvat = cv2.resize(kuvat, None, fx=0.5, fy=0.5)
#cv2.imwrite("kuvituskuvat/bitwise_or.jpg", kuvat)

cv2.imshow("kuvat", kuvat)
cv2.waitKey(0)