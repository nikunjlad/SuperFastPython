# import relevant libraries
import time, threading, psutil, sys
from concurrent.futures import ThreadPoolExecutor

# function to simulate a write operation
class WriteSimulator:

    def __init__(self):
        
        # variable to hold number of physical CPU cores present on the system
        self.physical_cores = psutil.cpu_count(logical=False)  

        # Lambda function to check if the number of default workers spun is the same as that of (2 times the physical CPU + 4)
        self.check_default_workers = lambda a : a == (2 * self.physical_cores) + 4  

    def task(self, value):

        # Print a message
        print(f"Saving file {value} to disk!")

        # wait to simulate a write operation to disk
        time.sleep(1)

    def initializer(self, arg1):

        print(f"Initializing {arg1} worker...")

# protect entry point
if __name__ == "__main__":

    # create an object to write files to disk
    ws = WriteSimulator()

    # Create a default Executor
    exe = ThreadPoolExecutor()

    # confirm that the default executor worker pool == (2 * physical CPU cores + 4)
    if ws.check_default_workers(exe._max_workers):
        print("Default worker threads created by ThreadPoolExecutor is equal to double the physical CPU cores plus 4")
    else:
        print("Default worker threads created by the ThreadPoolExecutor is not equal to double the physical CPU cores plus 4")

    # create a custom ThreadPoolExecutor with number of workers equal to the Physical CPU cores
    with ThreadPoolExecutor(max_workers=ws.physical_cores, initializer=ws.initializer, initargs=("Writer",), thread_name_prefix="WriterWorker") as exe2:
        
        # execute 100 write operations on pool of 8 worker threads (since number of physical CPU on system is 8)
        _ = exe2.map(ws.task, range(100))



        


