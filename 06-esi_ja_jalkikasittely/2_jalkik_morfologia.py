"""Esimerkki eri morfologiafunktioiden käytöstä erimuotoisilla 
rakenne-elementeillä"""

import cv2
import numpy as np

kuva = cv2.imread("06-esi_ja_jalkikasittely/seamk_logo.jpg", 0)
_, kuva = cv2.threshold(kuva, 100, 255, cv2.THRESH_BINARY)

# Määritellään käytettävät operaatiot, muodot ja koot
operaatiot = {"eroosio": cv2.MORPH_ERODE, 
              "dilaatio": cv2.MORPH_DILATE, 
              "avaaminen": cv2.MORPH_OPEN, 
              "sulkeminen": cv2.MORPH_CLOSE}
muodot = [cv2.MORPH_RECT, cv2.MORPH_ELLIPSE, cv2.MORPH_CROSS]
koot = [5, 11]

# Rullataan kaikki operaatiot, muodot ja koot silmukassa.
for nimi, op in operaatiot.items():
    for i, koko in enumerate(koot):
        kuvat = kuva.copy()
        # Samalle rakenne-elementillä tehdään kaikki määritellyt operaatiot
        # kaikilla määritellyillä koilla.
        for muoto in muodot:
            rel = cv2.getStructuringElement(muoto, (koko, koko))
            kuva_kas = cv2.morphologyEx(kuva, op, rel)
            # Eri operaatioiden tulokset allekkain.
            kuvat = np.vstack((kuvat, kuva_kas))
        # Ja eri kokojen tulokset (kaikilla operaatioilla) vierekkäin
        if i == 0:
            koko_kuva = kuvat.copy()
        else:
            marginaali = np.zeros((kuvat.shape[0], 50), "uint8")
            koko_kuva = np.hstack((koko_kuva, marginaali))
            koko_kuva = np.hstack((koko_kuva, kuvat))
    
    #cv2.imwrite(f"kuvituskuvat/morfologia_{nimi}.jpg", koko_kuva)
    cv2.imshow(f"{nimi} koilla {koot}", koko_kuva)
    cv2.waitKey(0)


