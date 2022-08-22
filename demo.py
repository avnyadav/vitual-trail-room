import cv2
import numpy as np


cap = cv2.VideoCapture(0)


while True:


    ret, frame = cap.read()

    cv2.imshow('frame',frame)

    np.ones_like(frame)
    cv2.imshow('frame1', np.ones_like(frame)*100)



    if cv2.waitKey(1) & 0xFF==ord('q'):
        break


cap.release()
cv2.destroyAllWindows()