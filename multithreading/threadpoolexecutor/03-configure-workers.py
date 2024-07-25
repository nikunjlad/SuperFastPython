# import relevant libraries
from concurrent.futures import ThreadPoolExecutor
import time, threading

# custom task function
def task(number):

    # block for a moment
    time.sleep(10)

    if number % 100 == 0:
        print(f"Task {number} done!")

# protect the entrypoint
if __name__ == "__main__":

    # create a thread pool
    with ThreadPoolExecutor(1000) as exe:
        
        # issue many tasks to the pool
        _ = exe.map(task, range(1000))

        print(threading.active_count())



