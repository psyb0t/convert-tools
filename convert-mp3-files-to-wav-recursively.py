#!/usr/bin/env python3
import glob
import os
from subprocess import check_call


def convert_files_in_dir(dir):
    for mp3file in glob.glob(os.path.join(dir, "*.mp3")):
        wavfile = "%s.wav" % os.path.splitext(mp3file)[0]

        check_call(["ffmpeg", "-i", mp3file, wavfile])


if __name__ == "__main__":
    convert_files_in_dir("./")

    for root, dirs, files in os.walk("./", topdown=False):
        for dir in dirs:
            convert_files_in_dir(os.path.join(root, dir))
