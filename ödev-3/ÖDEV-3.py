import cv2
import numpy as np

img_path = r"C:\Users\mtdev\OneDrive\Masaüstü\ödev-3\Pirinç_resmi.jpg"
img = cv2.imread(img_path)

scale_percent = 50
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resized_img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

_, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

sure_bg = cv2.dilate(opening, kernel, iterations=3)
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
_, sure_fg = cv2.threshold(dist_transform, 0.3 * dist_transform.max(), 255, 0)
sure_fg = np.uint8(sure_fg)

unknown = cv2.subtract(sure_bg, sure_fg)

_, markers = cv2.connectedComponents(sure_fg)
count = markers.max()

markers = cv2.watershed(resized_img, markers)
resized_img[markers == -1] = [255, 0, 0]

cv2.putText(resized_img, f"Pirinc Taneleri Sayisi: {count}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

cv2.imshow('Küçültülmüş Orijinal Resim', resized_img)
cv2.waitKey(0)
cv2
