import webbrowser
import time

for i in range(1, 4):
    print("This program started on" + time.ctime())
    time.sleep(2) #time is in seconds 
    webbrowser.open("www.google.ca")
    
