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
    tomorrow = str(datetime.date.today() + datetime.timedelta(days=1) ).replace("-","_")
    path2create = path+"/"+tomorrow
    try:
        os.mkdir(path2create)
    except:
        pass
    return path2create

def return_tasks_list(file, path):
    """Returns the text information of the file in the path as a list of tasks
    """
    fpath = path + "/" + file
    f_open = open(fpath, "r")
    content = f_open.read().split("-[")
    return content

def get_updated_content_strings(content):
    """Returns two strings one with all the completed tasks for today and the other with tasks for tomorrow
    """
    contend_today = []
    content_yesterday = []

    for task in content:
        if task[0] == "]":
            contend_today.append(task.replace("]","-[]"))
        else:
            ctoday = task.replace("x]","-[x]")
            content_yesterday.append(ctoday)

    content_yesterday = "".join(content_yesterday)
    contend_today = "".join(contend_today)

    return content_yesterday, contend_today

def update_entries(file, path2yesterday, path2day):
    content = return_tasks_list(file, path2yesterday)
    content_yesterday, content_today = get_updated_content_strings(content)

    #update yesterday's file
    fy_path = path2yesterday + "/" + file
    f = open(fy_path, "w")
    yesterday_formatted = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%B %d, %Y")
    f.write("# "+str(yesterday_formatted))
    f.write("\n"+str(content_yesterday))
    f.close()

    #update today's file
    fpath = path2day + "/" + file
    f = open(fpath, "a")
    f.write("\n"+str(content_today))
    f.close()

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

        if file == "summary.md":
            f.write("\n\n## Done:\n\n\n")
            f.write("## Questions:\n\n\n")
            f.write("## Ideas:\n\n\n")
        f.close()


def update_files(file, project_root):
    yesterday = str(datetime.date.today() - datetime.timedelta(days=1) ).replace("-","_")
    path2yesterday = project_root+"/"+yesterday

    today = str(datetime.date.today()).replace("-","_")
    path2today = project_root+"/"+today

    update_entries(file, path2yesterday, path2today)


# main function
if __name__ == "__main__":
    project_root = "/Users/shanto/LFL/Summer22"
    files = ["summary.md","goals.md"]
    dir = create_dir(project_root)
    files_to_create(dir, files)
    update_files(files[1], project_root)


