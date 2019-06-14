import cv2
import numpy as numpy

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    cv2.rectangle(frame, (225, 381), (1027, 712), (255,0,0), 2)
    cv2.rectangle(frame, (416, 256), (805, 712), (255,0,0), 2)
    cv2.imshow('window',frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break 

