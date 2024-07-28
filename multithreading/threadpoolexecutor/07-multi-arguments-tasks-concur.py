# import relevant libraries
import random, time
from concurrent.futures import ThreadPoolExecutor

# custom function 
def task(number, value):
    
    # report a message
    print(f"Task generated {value}")

    # block for random value based interval
    time.sleep(value)

    # return a new value
    return value + number

if __name__ == "__main__":

    # create threadpool
    with ThreadPoolExecutor(4) as exe:

        # prepare a random number list
        values = [random.random() for _ in range(10)]

        # issue tasks concurrently
        for result in exe.map(task, range(10), values):

            # report results
            print(result)