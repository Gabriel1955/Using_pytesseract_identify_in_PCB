import pytesseract
from PIL import Image
import numpy as np
import cv2


def correcting_text(text):
    letters = ['R', 'C', 'P', 'U', 'Q']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


img = cv2.imread('c/c2.png')
(T, img) = cv2.threshold(img, 190, 255, cv2.THRESH_BINARY)
img = cv2.medianBlur(img, 7)
text = pytesseract.image_to_string(img, lang='myFont2')
font = cv2.FONT_HERSHEY_SIMPLEX
# org
org = (50, 50)
# fontScale
fontScale = 1
# Blue color in BGR
color = (255, 0, 0)
# Line thickness of 2 px
thickness = 2
print(text)
print(len(text))
img = cv2.putText(img, text, org, font,
                  fontScale, color, thickness, cv2.LINE_AA)
cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
