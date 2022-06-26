import random
import time

def show_intervals():
    i=0
    while i<10:

        n = random.randint(1,10)
        if  n>6 or n<4 :
            i=i+1
            print(n)    
            time.sleep(1) 
        else:
            i=i+1
            print("Value ERROR")
        

def main():
    show_intervals()

if __name__== "__main__" :
    main()
    