#!/usr/bin/python3
import autoScroll, checkActivation
import threading, time, os, logging
import configData

if __name__ == '__main__':

    #logging.basicConfig(level=logging.INFO)

    event = threading.Event()

    t1 = threading.Thread(target=autoScroll.Scroll, name='Auto_scrolling',args=(event,))

    t2 = threading.Thread(target=checkActivation.checkMousePosition, name='Check_Activation_Mouse',args=(event,))

    print ('Starting Program')

    t1.start()
    t2.start()
    time.sleep(1)

    while True:
        print ('Number of current thread is:', threading.activeCount())
        time.sleep(3)
