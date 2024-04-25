"""Esimerkki värien erottamisesta BGR-kuvasta tasojen (kanavien)
avulla"""

import cv2
import numpy as np

kuva = cv2.imread("05-varit/pallot.jpg")

# Eri värikanavat irralleen ja sitten samaan kuvaan. Jotta voidaan
# käyttää hstack-funktiota, pitää kuvatyyppi muuttaa yksikanavaisesta
# (harmaasävy) kolmikanavaiseen (värikuva).
b, g, r = cv2.split(kuva)
kuvat = np.hstack((kuva, cv2.cvtColor(b, cv2.COLOR_GRAY2BGR)))
kuvat = np.hstack((kuvat, cv2.cvtColor(g, cv2.COLOR_GRAY2BGR)))
kuvat = np.hstack((kuvat, cv2.cvtColor(r, cv2.COLOR_GRAY2BGR)))

# Käytetään threshold-funktiota binärisöintiin. Maskataan
# kuvaa saadulla sinisellä maskilla.
_, bmv = cv2.threshold(b, 100, 255, cv2.THRESH_BINARY)
b_maskattu = cv2.bitwise_and(kuva, kuva, mask=bmv)
kuva_bmv = np.hstack((cv2.cvtColor(bmv, cv2.COLOR_GRAY2BGR), b_maskattu))

# Luodaan uusi kuva ja hyödynnetään loogisia operaatioita maskin
# luomisessa. Maskataan.
bmv2 = np.zeros_like(b)
bmv2[b > 100] = 255
bmv2[g > 200] = 0
bmv2[r > 150] = 0
b2_maskattu = cv2.bitwise_and(kuva, kuva, mask=bmv2)
kuva_bmv2 = np.hstack((cv2.cvtColor(bmv2, cv2.COLOR_GRAY2BGR), b2_maskattu))

# # Talletetaan ja näytetään kuvat
# cv2.imwrite("kuvituskuvat/pallot_bgr.jpg", kuvat)
# cv2.imwrite("kuvituskuvat/pallot_b_kynnys.jpg", kuva_bmv)
# cv2.imwrite("kuvituskuvat/pallot_b2_kynnys.jpg", kuva_bmv2)

cv2.imshow("kuvat", kuvat)
cv2.imshow("kynnystetty sininen", kuva_bmv)
cv2.imshow("oma kynnys sininen", kuva_bmv2)
cv2.waitKey(0)