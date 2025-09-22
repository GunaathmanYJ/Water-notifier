import time
from plyer import notification
while True:
    print("Time to drink water 💧")
    notification.notify(title="Time to drink water",
                        message = "It's a good time to drink water")
    time.sleep(3600)
    
