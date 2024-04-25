""""Esimerkki OpenCV:n taustanpoistajaluokkien käytöstä"""

import cv2
 
#taustanPoistaja = cv2.createBackgroundSubtractorMOG2()
taustanPoistaja = cv2.createBackgroundSubtractorKNN()
 
cap = cv2.VideoCapture("02-laskutoimitukset/vtest.avi")

while True:
    ret, frame = cap.read()
    if frame is None:
        break

    maski = taustanPoistaja.apply(frame)
    maskattu = cv2.bitwise_and(frame, frame, mask=maski)

    cv2.imshow("ruutu", frame)
    cv2.imshow("maski", maski)
    cv2.imshow("maskattu", maskattu)

    # Toisto lopetetaan, kun näppäintä q painetaan
    if cv2.waitKey(30) & 0xFF == ord('q'): 
        break