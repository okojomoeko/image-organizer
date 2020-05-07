import datetime
import os
import shutil
import sys
import time
from pathlib import Path, PurePath
from datetime import datetime
"""
"""

def main():
    args = sys.argv
    if len(args) > 2:
        print("Too long arguments")
        exit()

    # List the files
    _path = Path(args[1]).iterdir()
    file_list = [p for p in _path if p.is_file()]
    if len(file_list) == 0:
        print("Could not find files")
        exit()

    # Varying functions by OS
    if os.name == "nt":
        def get_create_time(path):
            return path.stat().st_ctime
    elif os.name == "posix":
        def get_create_time(path):
            try:
                return path.stat().st_birthtime
            except:
                return path.stat().st_mtime

    temp_name = ""
    count = 0 # the count variable in case of duplication of image name
    for name in file_list:
        update_t = datetime.fromtimestamp(get_create_time(Path(name)))
        year = update_t.strftime("%Y")
        month = update_t.strftime("%m")
        day = update_t.strftime("%d")
        hour = update_t.strftime("%H")
        minuite = update_t.strftime("%M")
        second = update_t.strftime("%S")
        ext = name.suffix

        dirname = year + "-" + month + "-" + day
        save_path = ""

        if "jpg" in ext.lower() or "png" in ext.lower():
            # if the format is image, make "IMG" directory and set preffix as "IMG"
            pref = "IMG"
            if not Path(args[1] + "/IMG").is_dir():
                Path(args[1] + "/IMG").mkdir()
            save_path = args[1] + "/IMG/" + dirname
        elif "mp4" in ext.lower() or "mov" in ext.lower():
            # if the format is video, mainly mp4 or mov, make "VID" directory and set preffix as "VID"
            pref = "VID"
            if not Path(args[1] + "/VID").is_dir():
                Path(args[1] + "/VID").mkdir()
            save_path = args[1] + "/VID/" + dirname


        save_name1 = "{0}_{1}{2}{3}_{4}{5}{6}{7}".format(pref,
            year, month, day, hour, minuite, second, ext)
        save_name = ""

        if temp_name == save_name1:
            # Use the count variable if duplicate file name exists
            save_name = "{0}_{1}{2}{3}_{4}{5}{6}_{7}{8}".format(pref,
                year, month, day, hour, minuite, second, count, ext)
            count += 1
        else:
            save_name = save_name1
            count = 0

        Path(name).rename(args[1] + "/" + save_name)
        if not Path(save_path).is_dir():
            Path(save_path).mkdir()
        if not Path(save_path + "/" + save_name).exists():
            shutil.move(args[1] + "/" + save_name, save_path + "/" + save_name)
            print("Move to: " + save_path + "/" + save_name)
        else:
            print("Couldn't move: {0}", save_name)

        temp_name = save_name


if __name__ == "__main__":
    main()
