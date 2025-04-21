import threading
import time
import random

room = threading.Semaphore(4)
chopstick = [threading.Semaphore(1) for _ in range(5)]

def eat(phil):
    print(f"Philosopher {phil} is eating.")
    time.sleep(random.uniform(1, 2)) 

def philosopher(phil):
    room.acquire() 
    print(f"Philosopher {phil} has entered the room.")

    chopstick[phil].acquire() 
    chopstick[(phil + 1) % 5].acquire()  
    eat(phil)
    print(f"Philosopher {phil} has finished eating.")

    chopstick[(phil + 1) % 5].release()
    chopstick[phil].release()

    room.release() 

threads = []
for i in range(5):
    t = threading.Thread(target=philosopher, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
