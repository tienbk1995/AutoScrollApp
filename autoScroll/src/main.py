#!/usr/bin/python3
import onClick, autoScroll, waitEvent, checkActivation
import threading, time, os
import configData

if __name__ == '__main__':

    event = threading.Event()

    #t1 = threading.Thread(target=onClick.clickDetected, name='On_click_event', args=(event,))

    t2 = threading.Thread(target=autoScroll.Scroll, name='Auto_scrolling',args=(event,))

    t3 = threading.Thread(target=waitEvent.waitForEvent, name='Waiting_event',args=(event,))

    t4 = threading.Thread(target=checkActivation.checkMousePosition, name='Check_Activation_Mouse',args=(event,))

    print('Starting Program')

    #t1.start()
    t2.start()
    t3.start()
    t4.start()
    # Set flag to indicate all threads have been started
    configData.isStartedFlag = True 
    time.sleep(3)

    while True:
        # Check person is absent or not
        if configData.isStartedFlag == False and configData.eventFlag == False:
            # Starting again 
            #t1 = threading.Thread(target=onClick.clickDetected, name='On_click_event', args=(event,))
            t2 = threading.Thread(target=autoScroll.Scroll, name='Auto_scrolling',args=(event,))
            t3 = threading.Thread(target=waitEvent.waitForEvent, name='Waiting_event',args=(event,))
            #t1.start()
            t2.start()
            t3.start()
            # Set flag to indicate all threads have been started
            configData.isStartedFlag = True

        print('Number of current thread is:', threading.activeCount())
        time.sleep(3)
        print ("Main:",configData.eventFlag)
