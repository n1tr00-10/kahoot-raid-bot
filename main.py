import asyncio
from kahoot import KahootClient
import random
import threading
import time

async def join_one(pin, name, retry=2):
    for attempt in range(retry):
        try:
            client = KahootClient()
            await client.join_game(pin, name)
            print(f"{name} joined")
            return True
        except:
            await asyncio.sleep(0.1)
    return False

def worker(pin, name):
    asyncio.run(join_one(pin, name))

def raid(pin, total):
    threads = []
    for i in range(total):
        name = f"n1tr00{random.randint(1000,9999)}"
        t = threading.Thread(target=worker, args=(pin, name))
        t.start()
        threads.append(t)
        time.sleep(0.1)
    
    for t in threads:
        t.join()
    
    print(f"\nRaid complete")

if __name__ == "__main__":
    pin = input("enter the kahoot game pin ").strip()
    count = int(input("how many bots "))
    raid(pin, count)
