import pyautogui, sys, threading, time, os, logging
import configData

def Scroll(event):
    try:
        threadID = threading.current_thread().getName()
        print (threadID,':Starting\r\n')
        time.sleep(1)
        while True:
            if configData.sampleCounter == 100:
                print (threadID, "Start scrolling\r\n")
                pyautogui.scroll(-10)
                pyautogui.time.sleep(1)
    except KeyboardInterrupt:
        print (threadID, ":Ctrl + C, stop scrolling\r\n")