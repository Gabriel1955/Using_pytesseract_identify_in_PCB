import cv2
import numpy as np
import pytesseract


font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
color = (255, 0, 0)
thickness = 2


def index(caracter):
    caracteres = ['R', 'C', 'P', 'U', 'Q', '0',
                  '1', '2', '3', '4', '5', '6', '7', '8', '9']
    try:
        caracteres.index(caracter)
        return True
    except:
        return False


mser = cv2.MSER_create()
img = cv2.imread('outputs_filtered/c3.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
buffer = img.copy()
regions, boxes = mser.detectRegions(gray)

for box in boxes:
    x, y, w, h = box
    crop_img = img[y:y+h, x:x+w]
    text = pytesseract.image_to_string(
        crop_img, lang='myFont2', config='--psm 10')

    if index(text):
        cv2.rectangle(buffer, (x, y), (x+w, y+h), (0, 255, 0), 1)
        buffer = cv2.putText(buffer, text, (x, y), font,
                             fontScale, color, thickness, cv2.LINE_AA)
    #cv2.imshow('img', crop_img)
    # print(text)
    # if cv2.waitKey(0) & 0xFF == ord('q'):
    #    break
cv2.imshow('img', buffer)
cv2.waitKey(0)
