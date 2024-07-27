# import relevant libraries
import random, time
from concurrent.futures import ThreadPoolExecutor, TimeoutError

# custom function
def task(number):

    # generate a random value
    value = random.random()

    # report a message
    print(f"Task {number} generated value {value}")

    # block momentarily
    time.sleep(number + value)

    # return the value
    return value + number

if __name__ == "__main__":

    # create a thread pool
    with ThreadPoolExecutor(max_workers=4) as exe:
        try:

            for result in exe.map(task, range(10), timeout=2):
                print(result)

        except TimeoutError:
            print("Gave up! Took too long!")

    # report a message
    print("Waiting for tasks to complete...")