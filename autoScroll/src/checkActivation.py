import pyautogui, sys, threading, time, os, logging
import configData

def checkMousePosition(event):
    threadID = threading.current_thread().getName()
    print (threadID,':Starting\r\n')
    time.sleep(1)
    initPos = pyautogui.position()
    while True:
        currPos = pyautogui.position()
        if initPos != currPos:
            print (threadID, ':Normally operating, do nothing!!')
            initPos = currPos
            configData.sampleCounter = 0
            logging.debug (threadID, configData.sampleCounter)
        else:
            logging.info('%s'.format(threadID), ':Position halt, Starting again')
            configData.sampleCounter += 1
            time.sleep(0.1)
            print (threadID, configData.sampleCounter)
        # Reset Sample Counter if reaching threshold
        if configData.sampleCounter >= 100:
            configData.sampleCounter = 100