"""Esimerkki eri pehmennyssuotimien käytöstä"""

import cv2
import numpy as np

# Käydään läpi kaikki esimerkkikuvat ja pehmennetään niitä
# eri suotimilla
kernelin_koot = [3, 9, 21]    
kuva = cv2.imread("kuvituskuvat/manhattan.jpg")
kuvat = kuva.copy()
suodin = "bilateral"

for kernelin_koko in kernelin_koot:

    if suodin == "blur":
        kuva_pehm = cv2.blur(kuva, (kernelin_koko, kernelin_koko))
    elif suodin == "gaussian":
        kuva_pehm = cv2.GaussianBlur(kuva, (kernelin_koko, kernelin_koko), 0)
    elif suodin == "median":
        kuva_pehm = cv2.medianBlur(kuva, kernelin_koko)
    elif suodin == "bilateral":
        sigma_color = 75  # Verrannollinen siihen, kuinka kaukaiset värisävyt (värikartalla) sekoittuvat
        sigma_space = 75  # Verrannollinen siihen, kuinka kaukana olevien pikselien värisävyt sekoittuvat

        kuva_pehm = cv2.bilateralFilter(kuva, kernelin_koko, sigma_color, sigma_space)
    else:
        raise ValueError(f"Suodintyyppiä '{suodin}' ei tunnistettu!")
    
    kuvat = np.hstack((kuvat, kuva_pehm))

#cv2.imwrite(f"kuvituskuvat/pehmennys_{suodin}.jpg", kuvat)
cv2.imshow("valmis", kuvat)
cv2.waitKey(0)