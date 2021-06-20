import pyautogui, sys, threading, time, os
import configData

def checkMousePosition(event):
    threadID = threading.current_thread().getName()
    print (threadID,':Starting\r\n')
    time.sleep(1)
    initPos = pyautogui.position()
    while True:
        currPos = pyautogui.position()
        if initPos != currPos:
            initPos = currPos
            print (threadID, ':Normally operating, do nothing!!')
        else:
            print (threadID, ':Position halt, Starting again')
            configData.eventFlag = False
        time.sleep(30)