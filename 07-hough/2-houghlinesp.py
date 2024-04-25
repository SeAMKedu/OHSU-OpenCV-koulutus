"""Esimerkki probabilistisesta Hough-muunnoksesta 
(Houghin viivamuunnoksesta)"""

import cv2
import numpy as np

kuva = cv2.imread("07-hough/pilvenpiirtaja.jpg")
kuva_hs = cv2.cvtColor(kuva, cv2.COLOR_BGR2GRAY)

# Etsitään reunat
#kuva_hs = cv2.medianBlur(kuva_hs, 5) # Pehmennä, jos tarpeen
reunakuva = cv2.Canny(kuva_hs, 100, 200)
cv2.imshow("reunat", reunakuva)

# Etsitään suorat
rho_reso = 1 # Yhden pikselin toleranssi
theta_reso = np.pi / 180 # Asteen tarkkuus
min_pisteet = 100 # Suoran toteuttavien pisteiden minimimäärä

suorat = cv2.HoughLinesP(reunakuva, 
                         rho_reso, 
                         theta_reso, 
                         min_pisteet,
                         minLineLength=50,
                         maxLineGap=10)
valmis = np.hstack((kuva, cv2.cvtColor(reunakuva, cv2.COLOR_GRAY2BGR)))

# Tieto kuvan koosta piirtoa varten
rivit, sarakkeet = kuva_hs.shape
lavistaja = int(np.sqrt(rivit**2 + sarakkeet**2))

# Käsitellään kaikki saadut rho - theta-parit ja piirretään
# niiden määrittelemät suorat
if suorat is not None:
    for s in suorat:
        x1,y1,x2,y2 = s[0]
        cv2.line(kuva, (x1, y1), (x2, y2), (0, 0, 255), 2)

valmis = np.hstack((valmis, kuva))
#cv2.imwrite("kuvituskuvat/houghp_pilvenpiirtaja.jpg", valmis)
cv2.imshow("tulos", kuva)
cv2.waitKey(0)
cv2.destroyAllWindows()