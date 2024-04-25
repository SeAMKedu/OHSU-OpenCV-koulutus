"""Esimerkki objektien analyysistä harmaasävykuvasta 
ääriviivoja hyödyntämällä"""

import cv2
import numpy as np

# Luetaan kuva kovalevyltä. Jos kuva tai kuvakansio on samassa 
# hakemistossa kuin kooditiedosto, riittää suhteellinen polku.
# Nyt imread lukee komponentit.png-nimisen kuvan samasta hakemistosta
# kuin missä kooditiedosto on. Jos kuvan lukeminen epäonnistuu
# (polku on virheellinen), kuvan arvoksi tulee None
kuva = cv2.imread("04-harmaasavykuva/komponentit.png")
if kuva is None:
    print("Kuvan lukeminen epäonnistui. Tarkista kuvapolku")
else:
    # Muutetaan harmaasävykuvaksi ja edelleen mustavalkokuvaksi.
    kuva_hs = cv2.cvtColor(kuva, cv2.COLOR_BGR2GRAY)
    kynnys, kuva_mv = cv2.threshold(kuva_hs, 100, 255, cv2.THRESH_BINARY)

    cv2.imshow("mustavalko", kuva_mv)

    # Etsitään reunaviivat
    reunaviivat, hierarkia = cv2.findContours(kuva_mv, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Tuloksena saatu muuttuja 'reunaviivat' on lista reunaviivojen x-y-
    # koordinaateista. Siinä on siis yhtä monta x-y-pistetaulukkoa kuin
    # reunaviivoja.
    # Käydään reunaviivat yksitellen läpi for-silmukassa. Lasketaan
    # jokaisen niistä pinta-ala. Jos pinta-ala ylittää 1000 neliöpikseliä,
    # piirretään reunaviiva alkuperäiseen värikuvaan punaisella.
    tuloskuva = np.zeros_like(kuva_mv)
    for reunaviiva in reunaviivat:
        if cv2.contourArea(reunaviiva) > 1000:
            cv2.drawContours(kuva, [reunaviiva], -1, (0, 0, 255), 5)
            cv2.drawContours(tuloskuva, [reunaviiva], -1, 255, -1)

    # Näytetään lopputulos ja odotetaan käyttäjältä näppäimen painallusta.
    cv2.imshow("kuva", kuva)
    cv2.imshow("vain isot", tuloskuva)
    cv2.waitKey(0)