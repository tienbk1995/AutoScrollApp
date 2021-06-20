import win32api, time, threading
import configData

#Button key list
LEFTMOUSE = 0x01
RIGHTMOUSE = 0x02
SCROLLMOUSE = 0x04
BACKSPACE = 0x08
TABSPACE = 0x09
ENTERKEY = 0x0D

def clickDetected(event):
    threadID = threading.current_thread().getName()
    print (threadID,'Starting\r\n')
    time.sleep(1)
    initPressedButton = win32api.GetKeyState(ENTERKEY)
    
    while configData.eventFlag == False:
        currPressedButton = win32api.GetKeyState(ENTERKEY)

        if currPressedButton != initPressedButton:
            initPressedButton = currPressedButton
            print ('Enter is pressed')
            event.set()

        time.sleep(2)
        print ("%s : %s" % (threadID, configData.eventFlag))