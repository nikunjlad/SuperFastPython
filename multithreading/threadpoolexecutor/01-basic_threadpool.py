from concurrent.futures import ThreadPoolExecutor
import time


def task():

    time.sleep(10)
    print("This is another thread!")

if __name__ == "__main__":
    
    # create threadpool
    with ThreadPoolExecutor() as exe:

        # issue a task
        future = exe.submit(task)

        print(future.running())
        
        # wait for the task to finish
        future.result()

        

        
