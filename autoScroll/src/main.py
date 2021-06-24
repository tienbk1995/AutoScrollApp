#!/usr/bin/python3
import autoScroll, checkActivation
import threading, time, os, logging, inspect
import configData

#Class to create threads
class CreateThreads(threading.Thread):
    def __init__(self, target=[], name=[], args=()):
        self._target = target
        self._name = name
        super().__init__(None, target, name, args)
    #To start all threads in the given list thread
    def StartAll(self):
        for index in range(len(self._target)):
            thread = CreateThreads(target=self._target[index], name=self._name[index], args=tuple(inspect.getargspec(self._target[index]).args))
            thread.start()
    #To start one given thread
    def StartOne(self, func, nameFunc):
        thread = CreateThreads(target=func, name=nameFunc, args=tuple(inspect.getargspec(func).args))
        thread.start()

if __name__ == '__main__':

    #logging.basicConfig(level=logging.INFO)
    # List thread given
    targetFuncs = [autoScroll.Scroll, checkActivation.checkMousePosition]
    # List name given
    nameFuncs = ['Auto_scrolling', 'Check_Activation_Mouse']
    # To init all given threads
    Threads = CreateThreads(targetFuncs, nameFuncs)
    # To create event synchronation
    event = threading.Event()

    print ('Starting Program')

    Threads.StartAll()
    
    time.sleep(1)

    while True:
        print ('Number of current thread is:', threading.activeCount())
        time.sleep(3)
