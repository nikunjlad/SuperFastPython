# import relevant libraries
import time
from concurrent.futures import ThreadPoolExecutor

# custom function to be executed in thread
def task(number):

    # report a message
    print(f"Worker executing task: {number}")

    # block momentarily
    time.sleep(1)

# initialize the worker in the thread pool
def init(arg1):

    # report a message
    print(f"Initializing {arg1} worker..")

# protect entry point
if __name__ == "__main__":

    # create and configure the ThreadPool
    with ThreadPoolExecutor(2, initializer=init, initargs=("LLM",)) as exe:
        
        # issue tasks into the pool
        _ = exe.map(task, range(4))
