import threading
import time
import random

NUM_PRINTERS = 3
semaphore = threading.BoundedSemaphore(NUM_PRINTERS)

def print_job(job_id):
    print(f"{job_id} waiting for a printer...")
    
    semaphore.acquire()
    try:
        print(f"{job_id} printing...")
        time.sleep(random.uniform(0.5, 1.5))
        print(f"{job_id} done.")
    finally:
        semaphore.release()

def submit_jobs():
    threads = []
    for i in range(10):
        t = threading.Thread(target=print_job, args=(f"Job-{i}",))
        threads.append(t)
        t.start()
        time.sleep(random.uniform(0.1, 0.3))
    
    for t in threads:
        t.join()

if __name__ == "__main__":
    submit_jobs()
    print("All jobs complete.")
