"""
This file contains helper functions for the main code

"""

# import relevant libraries
import argparse, traceback, os, cv2

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


# function to set argument parsing
def configure_argparse():

    # create commandline argument parser
    try:
        ag = argparse.ArgumentParser()
        ag.add_argument("-f", "--fast", action="store_true", help="this argument")
        args = vars(ag.parse_args())
    except Exception as e:
        traceback.printexc()

    return args

def getImageInfo(img_no, image_file):

    # read an image file from disk
    img = cv2.imread(image_file)

    # print the image resolution
    print(f"Image {img_no} has size {img.shape}")
