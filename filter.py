import cv2

imgInput = cv2.imread("motherboards/placa2.jpg", 0)
imgInput = cv2.adaptiveThreshold(imgInput, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY, 11, -2)
imgInput = cv2.medianBlur(imgInput, 7)

cv2.imwrite("Outputs_tests_filters/saida_teste2.jpg", imgInput)
