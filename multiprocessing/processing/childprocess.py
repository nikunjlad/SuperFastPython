import time
import multiprocessing
import psutil
import os

def task():

    # block for a moment
    time.sleep(1)

    # print a message
    print(f"Child process: {process.name} \nChild PID: {process.pid} \nChild's Parent: {psutil.Process(process.pid).ppid()}", flush=True)


if __name__ == "__main__":

    print(f"Parent process: {multiprocessing.current_process().name} \nParent PID: {os.getpid()} \n-------------------")

    start_time = time.time()

    # create a multiprocessing child process and assign it a function to execute
    process = multiprocessing.Process(target=task)

    # start the process
    process.start()

    # print a message
    print(f"Child process started \n--------------------")


    # wait for the child process to finish by joining it to our main process
    process.join()

    print(f"Execution time: {time.time() - start_time} secs")

