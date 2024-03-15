import pyautogui
from PIL import ImageGrab
import cv2
import numpy as np
import pytesseract
from screeninfo import get_monitors
#could work with hashes for id specific

#Capture area on desktop through PIL ImageGrab 
#Using pyTesseract try to find numbers in the image and process it into data


def processImage():
    #For practical use you will need to fiddle with this to place the box around the data you want.
    bpadding = 250
    lpadding = 250
    width, height = (200, 200)

    
    x, y = pyautogui.size()
    y -= height + bpadding
    x = lpadding



    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
    screenshot.save('test.png')

    image = cv2.imread('test.png')

    #If some numbers are being missed or misread you can change some values HERE
    #For example besides "gray = cv2.COLOR_BGR2HSV" you can try other color transforms

    alpha = 1.3
    brightenedI = cv2.addWeighted(image, alpha, np.zeros_like(image), 0, 0)

    gray = cv2.cvtColor(brightenedI, cv2.COLOR_BGR2HSV)

    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    cv2.imwrite('processedTest.png', binary)

    text = pytesseract.image_to_string(binary)

    #HERE--------------^^

    numbers = [[int(num) for num in row if num.isdigit()] for row in text.splitlines()]
    numbers = [row for row in numbers if row]

    result = []
    def convert(arr):
        if len(arr) >= 2:
            decP = arr[-2:]
            intP = arr[:-2]
            integerP = str(''.join(map(str, intP)))
            decimalP = str(''.join(map(str, decP)))
            floatV = float(f"{integerP}.{decimalP}")

            result.append(floatV)

    for num in numbers:
        convert(num)

    return result

print(processImage())
