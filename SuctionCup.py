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
# #disconnect
# state = dType.DisconnectDobot(api)

####################
#devType: ML
#isUsingRail: False
dType.SetQueuedCmdClear(api) #Clear the queue
dType.SetQueuedCmdStartExec(api) #Start the queu
dType.SetQueuedCmdStopExec(api) #Stop the que
dType.SetArmSpeedRatio(api,1,60, 1)
dType.SetPTPJumpParams(api,20.0,100.0, 1)
dType.SetLostStepParams(api,5.0, 1)

HOME = {
    dType.DobotConnect.DobotConnect_NoError:  "connected",
    dType.DobotConnect.DobotConnect_NotFound: "not connected",
    dType.DobotConnect.DobotConnect_Occupied: "occupied"}

dType.SetHOMEParams(api,240, 0, 150, 0, isQueued=1 )
index = dType.SetHOMECmd(api, 1, 1)

for i in range(0, 1):
    dType.SetPTPCmdEx(api,1 ,240.1369, 0.0, 151.5089, 0.0, 1)
    dType.SetEndEffectorSuctionCupEx(api,0,0, 1)
    dType.SetPTPCmdEx(api,1 ,344.8, -100, -10.0, 0.0, 1)
    dType.SetEndEffectorSuctionCupEx(api,0,0, 1)
    dType.SetPTPCmdEx(api,1 ,344.8, -100, -40.0, 0.0, 1)
    dType.SetEndEffectorSuctionCupEx(api,1,1, 1)
    dType.SetPTPCmdEx(api,1 ,344.8, -100, -10.0, 0.0, 1)
    dType.SetEndEffectorSuctionCupEx(api,1,1, 1)
    dType.SetPTPCmdEx(api,1 ,344.8, 100, -10.0, 0.0, 1)
    dType.SetEndEffectorSuctionCupEx(api,1,1, 1)
    dType.SetPTPCmdEx(api,1 ,344.8, 100, -40.0, 0.0, 1)
    dType.SetEndEffectorSuctionCupEx(api,0,0, 1)
    dType.SetPTPCmdEx(api,1 ,344.8, 100, -10.0, 0.0, 1)
    dType.SetEndEffectorSuctionCupEx(api,0,0, 1)
    dType.SetPTPCmdEx(api,1 ,324.8, -100, -10.0, 0.0, 1)
    dType.SetEndEffectorSuctionCupEx(api,0,0, 1)
    dType.SetPTPCmdEx(api,1 ,324.8, -100, -40.0, 0.0, 1)
    dType.SetEndEffectorSuctionCupEx(api,1,1, 1)
    dType.SetPTPCmdEx(api,1 ,324.8, -100, -10.0, 0.0, 1)
    dType.SetEndEffectorSuctionCupEx(api,1,1, 1)
    dType.SetPTPCmdEx(api,1 ,344.8, 100, -11.0, 0.0, 1)
    dType.SetEndEffectorSuctionCupEx(api,0,0, 1)
    dType.SetPTPCmdEx(api,1 ,344.8, 100, 0.0, 0.0, 1)
    dType.SetEndEffectorSuctionCupEx(api,0,0, 1)
    dType.SetPTPCmdEx(api,1 ,240.1369, 0.0, 151.5089, 0.0, 1)
    dType.SetEndEffectorSuctionCupEx(api,0,0, 1)
dType.dSleep(1000)
dType.RestartMagicBox(api)

###################
   
dType.SetPTPCmdEx(api,1 ,240, 0, 150, 0, 1)     # _,_,x,y,z,r,_
dType.SetPTPCmdEx(api,1 ,240, -102, -55, 0, 1)  # location_a
dType.SetEndEffectorSuctionCupEx(api,1,1, 1)    # on
dType.SetPTPCmdEx(api,1 ,240, 0, 150, 0, 1)     # _,_,x,y,z,r,_
dType.SetPTPCmdEx(api,1 ,341, -4, -55, 0, 1)  # location_e
dType.SetEndEffectorSuctionCupEx(api,0,0, 1)    # off
dType.SetPTPCmdEx(api,1 ,240, 0, 150, 0, 1)     # _,_,x,y,z,r,_

