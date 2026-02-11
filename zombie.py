import os
import time

pid = os.fork()

if pid == 0:
    print(f"Child ({os.getpid()}): Exiting immediately")
    os._exit(0)
else:
    print(f"Parent ({os.getpid()}) started")
    time.sleep(30)
    print(f"Parent ({os.getpid()}) finished")
