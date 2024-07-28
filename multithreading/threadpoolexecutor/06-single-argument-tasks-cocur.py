# import relevant libraries
import random, time
from concurrent.futures import ThreadPoolExecutor

# custom function 
def task(number):

    # generate a random number
    value = random.random()

    # report a message
    print(f"Task generated {value}")

    # block for random value based interval
    time.sleep(value)

    # return a new value
    return value + number

if __name__ == "__main__":

    # create threadpool
    with ThreadPoolExecutor(4) as exe:

        # issue tasks concurrently
        for result in exe.map(task, range(10)):

            # report results
            print(result)