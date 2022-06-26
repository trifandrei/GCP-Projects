import time
import threading
import multiprocessing

def print1():
   pass
    

def pr1():
    t1 = threading.Thread(target=print1(), args=(10,))
    t2 = threading.Thread(target=print1(), args=(10,))
    t3 = threading.Thread(target=print1(), args=(10,))
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
   

def main():

    p1 = multiprocessing.Process(target=pr1, args=( ))
    p2 = multiprocessing.Process(target=pr1, args=( ))
    p3 = multiprocessing.Process(target=pr1, args=( ))
    p4 = multiprocessing.Process(target=pr1, args=( ))
    p5 = multiprocessing.Process(target=pr1, args=( ))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    
    time.sleep(120)
    
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()


if __name__ == "__main__":
    main()

