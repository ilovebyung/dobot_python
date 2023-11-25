'''
1. make a detection and stop conveyor belt
2. extract ROI and make a comparision  
3. get a center point of detected object
4. get a target point and pick & place object 

'''

##########################################################
######## 3. get a center point of detected object ########
##########################################################

import cv2
import numpy as np
from ultralytics import YOLO

# model = YOLO("yolov8m.pt") 
model = YOLO("best.pt")
cap = cv2.VideoCapture(1)
# # Release the capture  
# cap.release()

def detect_center():

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise ValueError("Unable to open video source")
    ret, frame = cap.read()
    result = model(frame)[0]

    # when a detection is made
    if result:
        for box in result.boxes:
            class_id = result.names[box.cls[0].item()]
            cords = box.xyxy[0].tolist()
            cords = [round(x) for x in cords]
            conf = round(box.conf[0].item(), 2)

            message = f"{class_id}, {cords}, {conf}"
            if conf > 0.8:
                # image = cv2.putText(frame, message , (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)

                start = cords[0:2]  # x1,y1
                end = cords[2:4]  # x2,y2
                x = (int(cords[0]) + int(cords[2]))/2
                y = (int(cords[1]) + int(cords[3]))/2
                center_point = np.array([int(x), int(y)])     
                print(center_point[0])
                return center_point


center_point = detect_center()
print(center_point)

###########################################################
###### 4.1. get a target point and pick ######
# transformation from the perspective of camera to robot
###########################################################

import numpy as np
from scipy.interpolate import NearestNDInterpolator

# Define the source and target points
source_points = np.array([
    [60, 150],
    [270, 150],
    [480, 150],
    [62, 360],
    [270, 360],
    [480, 355],
    [140,155],
    [400,150],
    [140,318],
    [340,315]
])

target_points = np.array([
    [343, 97],
    [340, 0],
    [342, -100],
    [244, 97],
    [244, 0],
    [244, -100],
    [340,56],
    [340,-60],
    [266,58],
    [265,-56]
])

# Create the NearestNDInterpolator object
interpolator = NearestNDInterpolator(source_points, target_points)



###########################################################
###### 4.2. pick & place object ######
###########################################################

# # Define the query points
# query_points = np.array([
#     [62, 360]
# ])

# Interpolate the query points
interpolated_values = interpolator(center_point)

print(interpolated_values)
x, y = interpolated_values[0] 

import DobotDllType as dType

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "connected",
    dType.DobotConnect.DobotConnect_NotFound: "not connected",
    dType.DobotConnect.DobotConnect_Occupied: "occupied"}
 
#Load Dll and get the CDLL object
api = dType.load()
 
#Connect Dobot
state = dType.ConnectDobot(api, "", 115200)[0]
print("Connect status:",CON_STR[state])

dType.SetPTPCmdEx(api,1 ,240, 0, 150, 0, 1)     # _,_,x,y,z,r,_
dType.dSleep(1000)
dType.SetPTPCmdEx(api,1 ,x, y, -55, 0, 1)  # location_a
dType.dSleep(1000)
dType.SetEndEffectorSuctionCupEx(api,1,1, 1)    # on
dType.dSleep(1000)
dType.SetPTPCmdEx(api,1 ,240, 0, 150, 0, 1)     # _,_,x,y,z,r,_
dType.dSleep(1000)
dType.SetPTPCmdEx(api,1 ,341, -4, -55, 0, 1)  # location_e
dType.dSleep(1000)
dType.SetEndEffectorSuctionCupEx(api,0,0, 1)    # off
dType.SetPTPCmdEx(api,1 ,240, 0, 150, 0, 1)     # _,_,x,y,z,r,_

############## run ####################
# x, y
center_point = detect_center()
print(center_point)
# interpolated x, y
interpolated_values = interpolator(center_point)
print(interpolated_values)
x, y = interpolated_values[0] 
# pick and place
dType.SetPTPCmdEx(api,1 ,240, 0, 150, 0, 1)     # _,_,x,y,z,r,_
# dType.dSleep(100)
dType.SetPTPCmdEx(api,1 ,x, y, -55, 0, 1)  # location_a
# dType.dSleep(100)
dType.SetEndEffectorSuctionCupEx(api,1,1, 1)    # on
dType.dSleep(100)
dType.SetPTPCmdEx(api,1 ,240, 0, 150, 0, 1)     # _,_,x,y,z,r,_
# dType.dSleep(100)
dType.SetPTPCmdEx(api,1 ,341, -4, -55, 0, 1)  # location_e
# dType.dSleep(100)
dType.SetEndEffectorSuctionCupEx(api,0,0, 1)    # off
dType.SetPTPCmdEx(api,1 ,240, 0, 150, 0, 1)     # _,_,x,y,z,r,_
