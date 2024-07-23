# THREAD POOL EXECUTOR

## 1. THREADS, EXECUTORS AND THREAD POOLS

### Introduction

- Thread : Smallest unit for program execution
- Each program is a process. A process has at least one thread for executing instructions. Main Thread is default thread when a python script is executed. When Python script is run it automatically starts a process and hence a main thread too.
- OS controls thread creation, execution and which CPU core is responsible for its execution
- Creating threads requires resources such as stack space. Computational cost of creating a thread is high if many ad-hoc tasks are going to be done. Re using threads can help by creating a pool of worker threads. 

### What is ThreadPool?

- Thread Pool : Pattern for managing a pool of worker threads
- Thread Pool features:
    - Controls when threads are created (only when needed)
    - Controls how many tasks each worker can execute
    - Controls what workers should do when not being used. 
- Worker Thread : Each thread in a pool is caller a worker. 
- Worker Threads can execute similar tasks or dissimilar tasks. In short, workers in a pool need not execute the same function but can execute any function and take any arguments as needed by the function. 
- Worker threads can raise exception in case of failure (without itself getting impacted by any error).

### What is ThreadPoolExecutor?

- This Class is present in the concurrent.futures module. It extends the Executor Class and returns a Future object
- Executor : 
    - Parent class of the ThreadPoolExecutor which defines basic life cycle of the pool
    - submit() : method to run a function inside a worker thread and which returns a Future object.
    - map() : Call a function for each item in the iterable provided. 
    - shutdown() : Shutdown the Executor. 
    - Executor started when class is created and needs to be shutdown explicitly (which will release resources).
    - submit() and map() used to submit tasks asynchronously.
- Future : 
    - Object returned when submitting tasks to the thread pool which may be completed later on. It represents a delayed result of an asynchronous task.
    - Future can also be called a promise or a delay. 
    - It provides context for result of a task which may or may not be executing. It is a way to get a result once it is available. 
    - Future objects cannot be created but can only be received once a task is assigned to worker using submit() method. 
    - cancelled() : function of a future object which if returns True indicates that the task was cancelled before being executed. 
    - running() : Returns True if task is currently running. 
    - done() : Returns True if task has completed or was canceled. 
    - A running task cannot be canceled and a done task could have been canceled. 
    - result() : access the result from the running task
    - exeception() : access any exception raised while running the task. 
- add_done_callback() : a callback function which is invoked by the task once its execution is completed by the threadpool

### When to use ThreadPoolExecutor


### Limitations of Threads in Python

### ThreadPoolExecutor for I/O bound tasks



