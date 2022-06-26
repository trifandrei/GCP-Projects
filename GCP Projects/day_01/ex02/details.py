import datetime
import platform

def get_details():
   print("Python version",platform.python_version())
   now = datetime.datetime.now()
   print("Current date and time: ",now.strftime("%d-%m-%Y %H:%M:%S"))
   
get_details()