"""
Created By: Ubaidullah Effendi-Emjedi
GitHub: https://github.com/Uncle-Uee
LinkedIn: https://www.linkedin.com/in/ubaidullah-effendi-emjedi-202494183/

Icon By: https://www.flaticon.com/authors/phatplus
Title: phatplus
"""

import os

from PIL import Image


def extract(images = []):
    """
    Extract Frames from a GIF
    :return:
    """
    for image in images:
        gif = Image.open(image)

        print(f"{image} has {gif.n_frames} frames.\n")

        for frame in range(0, gif.n_frames):
            gif.seek(frame)
            filename = image.replace(".gif", f"_{frame}.png")
            gif.save(f"{filename}")


def runtime():
    print("""
    This Program Extracts all the Frames of a GIF.
    To only Extract Frames from all the GIFs in the Current Working Directory, Enter 0.
    To Extract Frames from all existing GIFs in the Current Working Directory and all Sub-Directories, Enter 1.
    """)
    action = int(input("Extract: "))

    if action > 0:
        list_of_files = list()
        for (directory_path, directory_names, filenames) in os.walk(os.curdir):
            list_of_files += [os.path.join(directory_path, file) for file in filenames if ".gif" in file]
        extract(list_of_files)
    else:
        extract(images = list(file for file in os.listdir(os.curdir) if ".gif" in os.path.splitext(file)[1]))


if __name__ == "__main__":
    runtime()
    os.system("pause")
