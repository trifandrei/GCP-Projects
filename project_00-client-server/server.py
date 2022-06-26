import socket  
import time
import threading

# thread function
def print1(c,addr):
    print ('Connected to ', addr[0]) 
    c.send('I am the main server'.encode())
    c.close()

# next create a socket object
s = socket.socket()        

# reserve a port 
port = 8080          
 
# Next bind to the port
s.bind(('', port))        
print ("socket binded to %s" %(port))
 
# put the socket into listening mode
s.listen(5)    
print ("socket is listening")          

addrTime = {}

while True:
# Establish connection with client.
  c, addr = s.accept()    
  time_now = time.time()
  ant_time = addrTime.get(addr[0])

  if ant_time:
      diff = time_now - ant_time
   
      if diff < 3:
          print("Refusing to answer to ", addr[0], " because it made a request ", format(diff, ".6f")," seconds ago")
          upd_dict = {addr[0]: time_now}
          addrTime.update(upd_dict)
         
          c.close()
      else:
          upd_dict = {addr[0]: time_now}
          addrTime.update(upd_dict)

          #create thread for each client
          t1 = threading.Thread(target=print1, args=(c,addr,))
          t1.start()      
  else:
      addrTime[addr[0]] = time_now
    
      #create thread for each client
      t1 = threading.Thread(target=print1, args=(c,addr,))
      t1.start()
 
