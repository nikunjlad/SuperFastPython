from concurrent.futures import ThreadPoolExecutor

if __name__ == "__main__":

    exe = ThreadPoolExecutor()

    print(exe._max_workers)

    exe.shutdown()