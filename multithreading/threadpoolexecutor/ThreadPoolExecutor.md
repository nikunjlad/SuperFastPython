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

ThreadPoolExecutor is only to be used when:
    - Tasks can be defined as pure function aka they produce a result given an input and has no side-effects or change state of any other global variable.
    - The task can fit within a single Python function (making it simple and easy to understand)
    - The same task needs to be performed many times with different arguments or different input data
    - We need to call the same function for each object in a collection using a for-loop

### Limitations of Threads in Python

- Due to GIL (Global Interpreter Lock), we can only run one thread at a time within a Python process. 
- We can write concurrent code with threads in Python but we may not be able to execute our code in parallel due to this limitation.
- GIL is released by the Python Interpreter sometimes to allow other threads to run in parallel and this is only during I/O operation where a thread is blocked or waiting for an external task to finish.
- A thread performing an I/O operation is blocked for the duration of an external operation (read/write to disk, send/receive data over socket, etc). This gives the OS the chance to let other threads run while suspending this thread until it gets the control back from the external operation.

### Applications of I/O bound tasks

Below are some examples of I/O bound tasks where ThreadPoolExecutor can be used for performing I/O bound tasks

1. For ML application, where the model runs on a server and is waiting to receive requests from a client. The client can be an edge device or any other computer or IOT device. The client should send data to the server (which are features to input into the model running on the server). The features could be a list of numerical data (for classical ML models), or it could be image/video data (for vision based models running on the server), or text prompts to expect a response (a LLM model running on the server), etc. The threadpoolexecutor can be used to run a function whose sole task is to send this data to the server and get a response back. The response can be either displayed on screen, sent to another server or a website or simply be saved to disk to be later reviewed. This is one of the examples where a pool of worker threads could be used for an I/O bound operation.
2. Another application where ThreadPoolExecutor could be used against normal threads and ThreadPool is to obtain a future object for the tasks submitted in the pool and carry on the processing of next tasks while waiting for results to occur. For instance, imagine a real-time application where a camera is used to source images and those images are to be sent to a server for inference and getting results. ThreadPoolExecutor can be used to first restrict the pool size to a set number of workers. Secondly, the tasks submitted using ad-hoc fashion can help us get future objects which we can keep periodically checking the status of the worker threads. If the worker finishes the job and results are available using the future object, we can do some sort of post-processing on the returned data. If say the server is slow, and all workers are busy, then we can still keep storing the incoming images into a queue without blocking the main thread from capturing the images from the camera. This will not only ensure the real-time nature of the system, but also, make sure we don't miss out on frames for inference by using queues which will help us send data to the thread pool once they are free from their existing tasks. 

