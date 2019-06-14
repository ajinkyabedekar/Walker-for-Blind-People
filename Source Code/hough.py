import numpy as np
from PIL import ImageGrab
import cv2


def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

def draw_lines(img,lines):
    try:
        for line in lines:
            coords = line[0]
            cv2.line(img, (coords[0], coords[1]), (coords[2], coords[3]), [255,255,255], 3)
    except:
        pass

def process_img(original_image):
    processed_image = cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)
    processed_image = cv2.Canny(processed_image, threshold1=200, threshold2=300)
    processed_image = cv2.GaussianBlur(processed_image, (5,5), 0)
    vertices = np.array([[10,500],[10,300],[300,200],[500,200],[800,300],[800,500],
                         ], np.int32)
    processed_image = roi(processed_image, [vertices])
     #                          edges       rho   theta   thresh         # min length, max gap:        
    lines = cv2.HoughLinesP(processed_image, 1, np.pi/180, 180,     30,         15)
    draw_lines(processed_image,lines)
    return processed_image



cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    screen = np.array(frame)
    new_screen = process_img(screen)
    cv2.imshow('window', new_screen)
    #cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
        