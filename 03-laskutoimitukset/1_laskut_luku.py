"""Esimerkkiskripti yhteenlaskuista kuvan ja vakion välillä
käyttämällä +-operaattoria ja OpenCV:n add-funktiota"""

import cv2
import numpy as np
from os.path import join

kansio = "kuvituskuvat"
kuva = cv2.imread(join(kansio, "manhattan.jpg"))
kuva_hs = cv2.cvtColor(kuva, cv2.COLOR_BGR2GRAY)

# Demonstroidaan vakion laskemista kuvaan +-operaattorilla
# ja OpenCV:n omalla funktiolla
luku = 30
kuva1 = kuva + luku
kuva2 = cv2.add(kuva, luku)
kuva_hs1 = kuva_hs + luku
kuva_hs2 = cv2.add(kuva_hs, luku)

# Alkuperäinen ja tulos vierekkäin
kuvat1 = np.hstack((kuva, kuva1))
kuvat2= np.hstack((kuva, kuva2))
kuvat_hs1 = np.hstack((kuva_hs, kuva_hs1))
kuvat_hs2 = np.hstack((kuva_hs, kuva_hs2))

# cv2.imwrite(join(kansio, "manhattan_varit1.jpg"), kuvat1)
# cv2.imwrite(join(kansio, "manhattan_varit2.jpg"), kuvat2)
# cv2.imwrite(join(kansio, "manhattan_hs1.jpg"), kuvat_hs1)
# cv2.imwrite(join(kansio, "manhattan_hs2.jpg"), kuvat_hs2)

cv2.imshow("bgr suoraan", kuvat1)
cv2.imshow("hs suoraan", kuvat_hs1)
cv2.imshow("bgr funktiolla", kuvat2)
cv2.imshow("hs funktiolla", kuvat_hs2)
cv2.waitKey(0)