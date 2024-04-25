"""Esimerkki Houghin ympyrämuunnoksesta"""

import cv2
import numpy as np

kuva = cv2.imread("07-hough/kone.jpg")
kuva_hs = cv2.cvtColor(kuva, cv2.COLOR_BGR2GRAY)

# Ei tarvitse etsiä reunoja, mutta pitää pehmentää
kuva_hs = cv2.medianBlur(kuva_hs, 3, 0)

# Parametrit
herkkyys = 1
min_kp_et = 50 # Keskipisteiden minimietäisyys
canny_ylin = 200 # Cannyn ylempi kynnys
min_pisteet = 40 # Montako pistettä kehällä? (Tai ainakin verrannollinen siihen.)

# Etsintä
ympyrat = cv2.HoughCircles(kuva_hs, 
                           cv2.HOUGH_GRADIENT, 
                           herkkyys,
                           min_kp_et,
                           param1=canny_ylin,
                           param2=min_pisteet, 
                           minRadius=20,
                           maxRadius=50)

# Pyöristetään kokonaislukuihin ja piirretään
kuva_tulos = kuva.copy()
if ympyrat is not None:
    ympyrat = np.uint16(np.round(ympyrat))
    for y in ympyrat[0]:
        cv2.circle(kuva_tulos, (y[0], y[1]), y[2], (255, 0, 0), 2) # Kehä
        cv2.circle(kuva_tulos, (y[0], y[1]), 2, (0, 0, 255), 3) # Keskipiste

valmis = np.hstack((kuva, kuva_tulos))
#cv2.imwrite("kuvituskuvat/hough_ymp_kolikot.jpg", valmis)
cv2.imshow("ympyrät", valmis)
cv2.waitKey(0)
cv2.destroyAllWindows()