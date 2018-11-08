from time import *         #must import time module to use sleep function
from threading import *    #must import threading module to inherit Thread class
class hello(Thread):      #must inherit Thread class in order to make the class as multithreaded
    def run(self):       # must implement the method in the name of "run" since it has to be overridden from  thread class
        for i in range(5):
            print("hello")
            sleep(1)     # to print hello and make the hello class thread to wait for 1 sec so tat hi class thread can execute


class hi(Thread):     #must inherit Thread class in order to make the class as multithreaded
    def run(self):      # must implement the method in the name of "run" since it has to be overridden from  thread class
        for i in range(5):
            print("hi")
            sleep(1) # to print hi and make the hi class thread to wait for 1 sec so tat hello class thread can execute


t1 = hello()
t2 = hi()


t1.start()    #must call start method ,so tat run method can be called implicitly nd make it run as thread
sleep(0.2)    #tuned to wait every 0.2 sec so that hi and hello is printed alternatively
t2.start()

t1.join()    #we use join here so that the main thread waits until hello class thread is completed executing
t2.join()    #we use join here so that the main thread waits until hi class thread is completed executing

print("bye")  # since we use join this bye is printed only once ,hello and hi thread has completed execution

