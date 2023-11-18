import cv2
import numpy as np

def kirmizi_nesne_tespit(frame):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    alt_kirmizi = np.array([0, 120, 70])  
    ust_kirmizi = np.array([10, 255, 255])  

    mask = cv2.inRange(hsv_frame, alt_kirmizi, ust_kirmizi)

    kirmizi_nesne = cv2.bitwise_and(frame, frame, mask=mask)

    return kirmizi_nesne

kamera = cv2.VideoCapture(0)

while True:
    ret, kare = kamera.read()  

    kirmizi_nesne_kare = kirmizi_nesne_tespit(kare)

    cv2.imshow('Kırmızı Nesne Tespiti', kirmizi_nesne_kare)
    
    key = cv2.waitKey(1)
    if key == 27:  
        break

kamera.release()
cv2.destroyAllWindows()
