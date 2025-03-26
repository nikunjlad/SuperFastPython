"""
Creating a child process to execute a task

To create a CPU profile: py-spy record -o profile.svg -- python3 childprocess.py

"""

__author__ = "Nikunj Lad"


# import libraries
import time
import multiprocessing
import psutil
import os

# define a function to perform a task
def task():

    # block for a moment
    time.sleep(1)

    # print a message
    print(f"Child process: {process.name} \nChild PID: {process.pid} \nChild's Parent: {psutil.Process(process.pid).ppid()}", flush=True)

# protect entrypoint
if __name__ == "__main__":

    # to support executable scenarios
    multiprocessing.freeze_support()

    # print parent information
    print(f"Parent process: {multiprocessing.current_process().name} \nParent PID: {os.getpid()} \n-------------------")

    # start time profiling
    start_time = time.time()

    # create a multiprocessing child process and assign it a function to execute
    process = multiprocessing.Process(target=task)

    # start the process
    process.start()

    # print a message
    print(f"Child process started \n--------------------")


    # wait for the child process to finish by joining it to our main process
    process.join()

    # print execution time
    print(f"Execution time: {time.time() - start_time} secs")

