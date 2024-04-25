"""Skripti videotiedoston lukemiseen tai kuvan lukemiseen
webkameralta"""

import cv2 
    
#cap = cv2.VideoCapture(0) # webkamera
cap = cv2.VideoCapture("02-kuvien_lukeminen/vtest.avi") # Videotiedosto

# Yritetään lukea
if cap.isOpened() == False:
    print("Videon lukeminen ei onnistunut!")

# Jos lukeminen onnistuu, luetaan ruutu kerrallaan
while cap.isOpened(): 
    ret, frame = cap.read() 
    # Kun luettava loppuu, lopetetaan
    if ret == False:
        break
    else:  
        cv2.imshow('Frame', frame) 
        
    # Näppäin q lopettaa kesken
        if cv2.waitKey(40) & 0xFF == ord('q'): 
            break