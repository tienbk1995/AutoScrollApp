import threading
import time
  
def run():
    while True:
        print('thread running')
        global stop_threads
        if stop_threads:
            break
  
stop_threads = False
t1 = threading.Thread(target = run)
t1.start()
time.sleep(1)
stop_threads = True
# while True:
#    print('Number of current thread is:', threading.activeCount())
t1.join()
t1.start()
print('thread killed')