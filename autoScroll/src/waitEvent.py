import threading
import configData

def waitForEvent(event):
    threadID = threading.current_thread().getName()
    if  event.wait():
        configData.eventFlag = True
        print ("%s : %s" % (threadID, configData.eventFlag))