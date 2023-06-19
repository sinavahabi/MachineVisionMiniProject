'''
    Here by using different error handlers we will ensure integrity and verification of our dataset images in the following directory.
    I have wrote 4 sample functions which will help us do so:
    1-First function makes sure all of our images in dataset are valid and readable.
    2-Second function will skip "user_warning" error, which is not necessary by the way. Because our program will continue running and there won't be any serious problem to crash or stop our program.
    3-Third function will make sure all of our dataset file are image formatted, such as '.jpg', '.jpeg', '.png' or '.gif'.  
    4-Fourth function also is not necessary in this case, because we already specified our images size when we are generating our data and building our CNN model with it. 
'''


import warnings
from PIL import Image
import os


def check_integrity():
    # Checking the file integrity.
    dataset_dir = 'dataset/train/Dog'

    for filename in os.listdir(dataset_dir):
        try:
            image_path = os.path.join(dataset_dir, filename)
            with Image.open(image_path) as image:
                # Perform any necessary operations on the image
                # ...
                pass
        except (IOError, OSError) as e:
            print(f"Error processing {filename}: {e}")


def skip_warning():
    # Skipping user warning error.
    # Remove the warning filter temporarily
    warnings.filterwarnings("ignore", category=UserWarning)

    dataset_dir = 'dataset/train/Dog'

    for filename in os.listdir(dataset_dir):
        try:
            image_path = os.path.join(dataset_dir, filename)
            with Image.open(image_path) as image:
                # Perform any necessary operations on the image
                # ...
                pass
        except (IOError, OSError) as e:
            print(f"Error processing {filename}: {e}")

    # Restore the warning filter
    warnings.filterwarnings("default", category=UserWarning)


def check_format():
    # Checking the image files formats.
    supported_formats = ('.jpg', '.jpeg', '.png', '.gif')

    for filename in os.listdir("dataset/train/Dog"):
        if filename.lower().endswith(supported_formats):
            image_path = os.path.join("dataset/train/Dog", filename)
            try:
                with Image.open(image_path) as image:
                    # Perform operations on supported images
                    # ...
                    pass
            except (IOError, OSError) as e:
                print(f"Error processing {filename}: {e}")
        else:
            print(f"Skipping unsupported file: {filename}")


def check_size():
    # Checking image size and probable dimension issus (Unnecessary).
    target_size = (224, 224)  # Example target size

    for filename in os.listdir("dataset/train/Dog"):
        if filename.lower().endswith(".jpg"):
            image_path = os.path.join("dataset/train/Dog", filename)
            try:
                with Image.open(image_path) as image:
                    if image.size != target_size:
                        # Handle images with incorrect size
                        # ...
                        pass
            except (IOError, OSError) as e:
                print(f"Error processing {filename}: {e}")
        else:
            print(f"Skipping unsupported file: {filename}")

'''
    Remember you can pass your own directory path to "dataset_dir" variable.
    Note: you should be aware that in order to use each one of functions above you have to call (invoke) them.
    For example--> "check_integrity()" will call this function and runs its scripts.
'''
