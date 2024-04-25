"""HSV-avaruuden sävy - kylläisyys-kuvaajan piirto"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

toistot = 4 # Kuinka monta samaa sävypikseliä peräkkäin
savyt = np.arange(180, dtype="uint8") # kaikki sävyt
savyt = np.repeat(savyt, toistot) # toistetaan samoja arvoja (kuvaan kokoa)
kyllaisyydet = np.arange(256, dtype="uint8") # kaikki kylläisyydet
savyt2D, kyllaisyydet2D = np.meshgrid(savyt, kyllaisyydet) # luodaan taulukko

# Luodaan pitkä putki arvoa 255 
arvot = np.ones(len(savyt) * len(kyllaisyydet), dtype="uint8") * 255

# H-, S- ja V-arvot yhteen yksiulotteiseksi kolmikanavaiseksi
hsv_kuva = np.column_stack((savyt2D.ravel(), kyllaisyydet2D.ravel(), arvot))

# Muotoillaan kuvan muotoiseksi (2D) ja muunnetaan RGB-kuvaksi
# (koska plotataan matplotlibillä, joka käyttää RGB:tä)
hsv_kuva = hsv_kuva.reshape(256, toistot * 180, 3)
bgr_kuva = cv2.cvtColor(hsv_kuva, cv2.COLOR_HSV2RGB)

# Näytetään Pyplotissa, jotta saadaan arvoakselit
plt.figure()
plt.imshow(bgr_kuva)
plt.title("Eri sävyn ja kylläisyyden tuottamat värit (arvo V = 255)")
plt.xlabel("sävy (H)")
plt.ylabel("kylläisyys (S)")
# Muokataan sävyn näyttävä akseli
xticks = np.arange(0, toistot*180, toistot*10)
labels = np.arange(0, 180, 10)
plt.xticks(xticks, labels)
plt.show()