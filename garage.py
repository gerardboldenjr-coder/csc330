import threading
import time
import random

CAPACITY = 5
garage = []
condition = threading.Condition()

def arrive(car_id):
    with condition:
        while len(garage) >= CAPACITY:
            condition.wait()
        
        garage.append(car_id)
        print(f"{car_id} arrived.  Garage: {garage}")
        condition.notify_all()

def depart():
    with condition:
        while len(garage) == 0:
            condition.wait()
        
        car_id = garage.pop(0)
        print(f"{car_id} departed. Garage: {garage}")
        condition.notify_all()

def arrival_thread():
    for i in range(10):
        arrive(f"Car-{i}")
        time.sleep(random.uniform(0.1, 0.4))

def departure_thread():
    for _ in range(10):
        depart()
        time.sleep(random.uniform(0.2, 0.6))

if __name__ == "__main__":
    t1 = threading.Thread(target=arrival_thread)
    t2 = threading.Thread(target=departure_thread)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"Done. Final garage state: {garage}")
