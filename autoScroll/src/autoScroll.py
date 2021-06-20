import pyautogui, sys, threading, time
import configData

def Scroll(event):
    try:
        threadID = threading.current_thread().getName()
        print (threadID,'Starting\r\n')
        time.sleep(1)
        while configData.eventFlag == False:
            pyautogui.scroll(-10)
            pyautogui.time.sleep(1)
            print ("%s : %s" % (threadID, configData.eventFlag))
    except KeyboardInterrupt:
        print ("Stop scrolling\r\n")