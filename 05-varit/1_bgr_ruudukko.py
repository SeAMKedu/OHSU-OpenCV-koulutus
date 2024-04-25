"""
Skripti, joka luo ruudukon eri värejä. Jokaisessa ruudussa on lisäksi kyseisen
värin BGR-arvo kirjoitettuna.
"""

import cv2
import numpy as np

# Alustukset
kuvat = None
kuvarivi = None
koko = 65
rivin_pituus = 8
rivitetty = 0

# Silmukoidaan sinisen, vihreän ja punaisen arvoja. Piirretään neliön muotoinen
# kuva, joka on pelkkää kyseistä väriä.
for b in range(0, 255, 80):
    for g in range(0, 255, 80):
        for r in range(0, 255, 80):
            b_taso = np.ones((koko, koko), dtype="uint8") * b
            g_taso = np.ones((koko, koko), dtype="uint8") * g
            r_taso = np.ones((koko, koko), dtype="uint8") * r
            kuva = cv2.merge([b_taso, g_taso, r_taso])

            # Tekstin ylamarginaali
            ylamarg = 15
            
            # Sääntö sille, onko teksti mustaa vai valkoista. Riippuu
            # värin tummuudesta.
            if b + g + r <= 240 :
                tekstin_vari = (255, 255, 255)
            else:
                tekstin_vari = (0, 0, 0) 
            # Kirjoitetaan värin BGR kuvan päälle 
            cv2.putText(kuva, f"B={b}", (koko//8, ylamarg), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, tekstin_vari, 1)
            cv2.putText(kuva, f"G={g}", (koko//8, 2*ylamarg), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, tekstin_vari, 1)
            cv2.putText(kuva, f"R={r}", (koko//8, 3*ylamarg), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, tekstin_vari, 1)

            # Ensimmäisen kuvan tapauksessa luodaan uusi kuvarivi
            if kuvarivi is None:
                kuvarivi = kuva
            # Jos kuvarivi on jo luotu, lisätään kuva rivin jatkoksi.
            else:
                kuvarivi = np.hstack((kuvarivi, kuva))
            rivitetty += 1
            # Jos rivi tuli täyteen, lisätään rivi taulukkoon ja tyhjennetään
            # rivi
            if rivitetty == rivin_pituus:
                if kuvat is None:
                    kuvat = kuvarivi
                else:
                    kuvat = np.vstack((kuvat, kuvarivi))
                rivitetty = 0
                kuvarivi = None

cv2.imwrite("kuvituskuvat/bgr_savyja.jpg", kuvat)

cv2.imshow("valmis", kuvat)
cv2.waitKey(0)

