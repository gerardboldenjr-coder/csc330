import os
import time

pid = os.fork()

if pid == 0:  # Child process
    print(f"Child ({os.getpid()}): Working for 2 seconds...")
    time.sleep(2)
    print(f"Child ({os.getpid()}) finished")
else:  # Parent process
    print(f"Parent ({os.getpid()}) started")
    child_pid, status = os.wait()
    print(f"Parent ({os.getpid()}) finished")
