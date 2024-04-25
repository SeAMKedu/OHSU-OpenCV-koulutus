"""Esimerkki erilaisista laskuista kahden kuvan välillä"""

import cv2
import numpy as np
from os.path import join

kansio = "kuvituskuvat"
kuva = cv2.imread(join(kansio, "manhattan.jpg"))
kuva2 = cv2.imread(join(kansio, "satelliitti.jpg"))

# Värikuvien yhteenlaskut
summa = cv2.add(kuva, kuva2)
summa_painot = cv2.addWeighted(kuva, 0.5, kuva2, 0.5, 0)
summa_skaala = cv2.scaleAdd(kuva2, 0.5, kuva)
kuva_korvaus = kuva.copy()
kuva_korvaus[kuva2 > 30] = kuva2[kuva2 > 30]

# Harmaasävykuvien yhteenlaskut
kuva_hs = cv2.cvtColor(kuva, cv2.COLOR_BGR2GRAY)
kuva_hs2 = cv2.imread("laskutoimitukset/seamk_logo.jpg", 0)
summa_hs = cv2.add(kuva_hs, kuva_hs2)

# Kuvan vähennyslaskut
kuva_tyhja = cv2.imread("laskutoimitukset/huone_tyhja.jpg")
kuva_joku = cv2.imread("laskutoimitukset/huone_tunkeilija.jpg")
kuva_erotus = cv2.subtract(kuva_joku, kuva_tyhja)
kuva_abs_erotus = cv2.absdiff(kuva_joku, kuva_tyhja)
 
# Laittaminen vierekkäin
summakuvat_bgr = np.hstack((kuva, kuva2))
summakuvat_bgr = np.hstack((summakuvat_bgr, summa))

summakuvat_hs = np.hstack((kuva_hs, kuva_hs2))
summakuvat_hs = np.hstack((summakuvat_hs, summa_hs))

summat_skaala = np.hstack((summa_skaala, summa_painot))

huoneet = np.hstack((kuva_tyhja, kuva_joku))
erotukset = np.hstack((kuva_erotus, kuva_abs_erotus))

print(np.sum(kuva_abs_erotus))

# cv2.imwrite(join(kansio, "harmaasummat.jpg"), summakuvat_hs)
# cv2.imwrite(join(kansio, "bgrsummat.jpg"), summakuvat_bgr)
# cv2.imwrite(join(kansio, "skaalasummat.jpg"), summat_skaala)
# cv2.imwrite(join(kansio, "korvaus.jpg"), kuva_korvaus)
# cv2.imwrite(join(kansio, "huoneet.jpg"), huoneet)
# cv2.imwrite(join(kansio, "erotukset.jpg"), erotukset)

cv2.imshow("hs", summakuvat_hs)
cv2.imshow("bgr", summakuvat_bgr)
cv2.imshow("bgr skaalat", summat_skaala)
cv2.imshow("bgr korvaus", kuva_korvaus)
cv2.imshow("erotukset", erotukset)
cv2.imshow("Joo", cv2.resize(kuva, (800, 600)))
cv2.waitKey(0)

