import numpy as np
from PIL import ImageGrab
import cv2

#vidobj = cv2.VideoCapture(0)
#success, image = vidobj.read()

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    screen = np.array(frame)
    #screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
    cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
        