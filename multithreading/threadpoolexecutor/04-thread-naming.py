# import relevant libraries
import time, threading
from concurrent.futures import ThreadPoolExecutor

# custom task function to perform in the thread pool
def task(number):

    # block for a moment
    time.sleep(1)

# protect entry point of the code
if __name__ == "__main__":

    # create thread pool
    with ThreadPoolExecutor(max_workers=4, thread_name_prefix="Downloader") as exe:

        # issue many tasks to the pool
        _ = exe.map(task, range(20))

        # report all thread names
        for thread in threading.enumerate():
            print(thread)
            
