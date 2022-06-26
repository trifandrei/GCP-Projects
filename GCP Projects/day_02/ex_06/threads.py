import time
import threading
  
def print1():
    time.sleep(60)
    print("1")

def print2():
    time.sleep(120)
    print("2")
 
def print3():
    time.sleep(180)
    print("3")

def print4():
    time.sleep(240)
    print("4")
 

def print5():
    time.sleep(300)
    print("5")
 
  
if __name__ == "__main__":
   
    t1 = threading.Thread(target=print1(), args=(10,))
    t2 = threading.Thread(target=print2(), args=(10,))
    t3 = threading.Thread(target=print3(), args=(10,))
    t4 = threading.Thread(target=print4(), args=(10,))
    t5 = threading.Thread(target=print5(), args=(10,))
    t1.start()
    t2.start()  
    t3.start()
    t4.start()
    t5.start()
 
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

    while True:
        pass