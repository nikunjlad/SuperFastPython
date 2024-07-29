# import relevant libraries
import random, time
from concurrent.futures import ThreadPoolExecutor

# custom function to be executed
def task():

    # generate a random value
    value = random.random()

    # report a message
    print(f"Task generated {value}")

    # block momentarily 
    time.sleep(value)

    return value

if __name__ == "__main__":

    # create thread pool
    with ThreadPoolExecutor() as exe:

        # issue an asynchronous task
        future = exe.submit(task)

        # get result
        result = future.result()

        print(result)
