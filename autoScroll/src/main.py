#!/usr/bin/python3
import onClick, autoScroll, waitEvent
import threading, time
import configData

if __name__ == '__main__':

    event = threading.Event()

    t1 = threading.Thread(target=onClick.clickDetected, name='On_click_event', args=(event,))

    t2 = threading.Thread(target=autoScroll.Scroll, name='Auto_scrolling',args=(event,))

    t3 = threading.Thread(target=waitEvent.waitForEvent, name='Waiting_event',args=(event,))

    print('Starting Program')

    t1.start()
    t2.start()
    t3.start()
    time.sleep(3)
    while True:
        print('Number of current thread is:', threading.activeCount())
        time.sleep(3)
        print ("Main:",configData.eventFlag)