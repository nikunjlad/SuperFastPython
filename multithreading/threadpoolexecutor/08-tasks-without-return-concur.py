# import relevant libraries
import random, time
from concurrent.futures import ThreadPoolExecutor

# custom function 
def task(number):

    # generate a random number
    value = random.random()

    # report a message
    print(f"Task {number} generated value {value}")

    # block for random value based interval
    time.sleep(value)


if __name__ == "__main__":

    # create threadpool
    with ThreadPoolExecutor(4) as exe:

        # issue tasks concurrently
        _ =  exe.map(task, range(10))