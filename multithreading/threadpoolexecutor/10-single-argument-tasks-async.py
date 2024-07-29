# import relevant libraries
import random, time
from concurrent.futures import ThreadPoolExecutor

# custom function to be executed
def task(number):

    # generate a random value
    value = random.random()

    # report a message
    print(f"Task generated {value}")

    # block momentarily 
    time.sleep(value)

    return number + value

if __name__ == "__main__":

    # create thread pool
    with ThreadPoolExecutor() as exe:

        # issue an asynchronous task
        future = exe.submit(task, 100)

        # get result
        result = future.result()

        print(result)

