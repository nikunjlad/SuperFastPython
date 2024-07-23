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
- Future : Object returned when submitting tasks to the thread pool which may be completed later on. 

