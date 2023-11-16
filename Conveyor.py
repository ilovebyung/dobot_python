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
dType.SetQueuedCmdClear(api) #Clear the queue
dType.SetQueuedCmdStartExec(api) #Start the queue
dType.SetQueuedCmdStopExec(api) #Stop the queue
#Set motion parameter
dType.SetHOMEParams(api, 200, 200, 200, 200, isQueued = 1)
dType.SetPTPJointParams(api, 200, 200, 200, 200, 200, 200, 200, 200, isQueued = 1)
dType.SetPTPCommonParams(api, 100, 100, isQueued = 1)
#Calculate the speed pulses
STEP_PER_CIRCLE = 360.0 / 1.8 * 5.0 * 16.0
MM_PER_CIRCLE = 3.1415926535898 * 32.0
vel = float(10) * STEP_PER_CIRCLE / MM_PER_CIRCLE # speed pulses required for a conveyor speed of 10[mm/s] 
vel = float(0) * STEP_PER_CIRCLE / MM_PER_CIRCLE # speed pulses required for a conveyor speed of 0[mm/s]
#Set to vel[pulse/s] and start
dType.SetEMotorEx(api, 0, 1, int(vel), True)
#Run 5 seconds
dType.dSleep(5000)
#Stop
dType.SetEMotorEx(api, 0, 0, int(vel), True)    #isEnabled 0

