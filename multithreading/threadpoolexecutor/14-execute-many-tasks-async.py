# import relevant libraries
import random, time
from concurrent.futures import ThreadPoolExecutor

# custom function to be executed
def task(number):

    # generate random number
    value = random.random()

    # print a message
    print(f"Task {number} generate {value}")

    # block momentarily
    time.sleep(value)

    return value + number

if __name__ == "__main__":

    # create ThreadPool
    with ThreadPoolExecutor() as ex:

        # issue many tasks asynchronously
        futures = [ex.submit(task, i) for i in range(5)]

        # enumerate futures
        for future in futures:
            print(future.result())