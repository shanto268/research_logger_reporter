# -*- coding: utf-8 -*-
"""
========================================
Program : work_logger/workLogger.py
========================================
Summary:
    Creates a directory with the date of the day and creates summary and goals markdown files for that day
"""
__author__ =  "Sadman Ahmed Shanto"
__date__ = "05/23/2022"

import datetime
import os
import subprocess

# function definitions
def create_dir(path):
    """Creates the directory based on the day

    :path: path to project root
    :returns: the string of the unique directory in the project root

    """
    today = str(datetime.date.today() + datetime.timedelta(days=1) ).replace("-","_")
    path2create = path+"/"+today
    try:
        os.mkdir(path2create)
    except:
        pass
    return path2create

def files_to_create(path, files):
    """Creates the required files in the input directory

    :path: path to unique directory
    :files: files to be created
    """
    for file in files:
        try:
            fpath = "{}/{}".format(path,file)
            bashCommand = "touch {}".format(fpath)
            process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        except:
            pass
        f = open(fpath, "a")
        today_formatted = (datetime.date.today()+ datetime.timedelta(days=1)).strftime("%B %d, %Y")
        f.write("# "+str(today_formatted))
        f.close()


# main function
if __name__ == "__main__":
    project_root = "/Users/shanto/LFL/Summer22"
    files = ["summary.md","goals.md"]
    dir = create_dir(project_root)
    files_to_create(dir, files)


