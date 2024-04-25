import cv2

kuva = cv2.imread("kuvituskuvat/manhattan.jpg")

# Kuva ja sen viisi pienennystä pyramideja käyttäen
cv2.imshow("alkuperainen", kuva)
for kierros in range(5):
    kuva = cv2.pyrDown(kuva)
    cv2.imshow(f"kierros {kierros + 1}", kuva)

# Kuvan pienentäminen lukemalla joka toinen, kolmas, 
# neljäs tai viides rivi ja sarake
kuva_puolet = kuva[::2, ::2]
kuva_yhdeksasosa = kuva[::3, ::3]
kuva_16osa = kuva[::4, ::4]
kuva_25osa = kuva[::5, ::5]

cv2.imshow("puolikas", kuva_puolet)
cv2.imshow("kolmannes", kuva_yhdeksasosa)
cv2.imshow("neljännes", kuva_16osa)
cv2.imshow("viidennes", kuva_25osa)

cv2.waitKey(0)