from ultralytics import YOLO
import cv2
import numpy as np 

model = YOLO("best.pt")

cap = cv2.VideoCapture(1)
if not cap.isOpened():
    raise ValueError("Unable to open video source")

ret, frame = cap.read()
result = model(frame)[0]

for box in result.boxes:
    class_id = result.names[box.cls[0].item()]
    cords = box.xyxy[0].tolist()
    cords = [round(x) for x in cords]
    conf = round(box.conf[0].item(), 2)
    if conf > 0.8:
        # start = cords[0:2]  # x1,y1
        # end = cords[2:4]  # x2,y2
        # color = (0, 0, 255)
        x = (int(cords[0]) + int(cords[2]))/2
        y = (int(cords[1]) + int(cords[3]))/2
        center_point = np.array([int(x), int(y)])  
        print(center_point[0]) 
        frame = cv2.circle(frame, center_point, 4, (0, 0, 255), 4)

cv2.imshow('result image', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()