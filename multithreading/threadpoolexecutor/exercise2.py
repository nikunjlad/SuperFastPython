# import libraries
import time, cv2, os, sys, argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
sys.path.append(str(Path(__file__).parent.parent.parent))
from utils import ROOT_DIR, configure_argparse, getImageInfo

# protect entry point
if __name__ == "__main__":

    # create commandline argument parser
    args = configure_argparse()

    # load files
    image_dir = os.path.join(ROOT_DIR, "data")
    image_paths = [os.path.join(image_dir, file) for file in os.listdir(image_dir)]

    # in FAST mode, we use thread pools 
    if args["fast"]:

        start_time = time.time()    # start the timer

        # create thread pool of 4 workers
        with ThreadPoolExecutor(max_workers=4, thread_name_prefix="Image_loader") as exe:

            # execute each task by using map function
            _ = exe.map(getImageInfo, range(len(image_paths)), image_paths)
        
        print(f"Time taken: {time.time() - start_time} secs")

    else:   # slow mode using regular for loops
        start_time = time.time()
        for ind, img_path in enumerate(image_paths):
            getImageInfo(ind, img_path)

        print(f"Time taken: {time.time() - start_time} secs")
            