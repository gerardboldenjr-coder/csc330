import os
import time

pid = os.fork()

if pid == 0:
    print(f"Child ({os.getpid()}): Sleeping for 30 seconds...")
    print(f"Child's original parent PID: {os.getppid()}")
    time.sleep(30)
    print(f"Child ({os.getpid()}) finished")
else:
    print(f"Parent ({os.getpid()}) started")
    print(f"Parent ({os.getpid()}) finished")
