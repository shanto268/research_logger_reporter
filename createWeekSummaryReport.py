# -*- coding: utf-8 -*-
"""
=================================================
Program : work_logger/createSummaryReport.py
=================================================
Summary:
    - accumulates all the files from workLogger.py and creates pdf reports
"""
__author__ =  "Sadman Ahmed Shanto"
__date__ = "05/27/2022"


#libraries used
import numpy as np
import os, sys, datetime, glob, subprocess

def get_all_paths(base_path):
    global today
    all_paths = []
    # record today's date
    today = str(datetime.date.today()).replace("-","_")
    # find the path corresponding to today's dir
    path = base_path + "/" + today
    # calculate and find all the paths until the last 7 days
    for day in range(8):
        last_week_path = base_path + "/" + str(datetime.date.today() - datetime.timedelta(days=day)).replace("-","_")
        all_paths.append(last_week_path)

    # print("all_paths : {}".format(all_paths))
    return all_paths

def get_all_files(all_paths, files):
    all_files = []
    for path in all_paths:
        for file in files:
        #make sure the path exists
            try:
                # add all the required files to a list
                all_files.append(path+"/"+file)
            except:
                pass
    # sort the list by file name type
    all_files.sort(key = lambda x: x.split("/")[-1])
    # restructure the list based on the number of files
    all_files = np.array(all_files)
    all_files = np.array_split(all_files, len(files))
    return all_files

def create_file_dump(all_files, target_path):
    fnames = []
    line = "-"*3
    end_line = "\n"+line+"\n\n"

    for files in all_files:
        i = 0 # for single shot loop execution
        content = []
        for file in files:
            #creates the summary files with the correct name in the right directory
            while i < 1: #this loop executes once
                actual_file = file.split("/")[-1]
                fname = target_path + "/" + today + "_" + actual_file
                fnames.append(fname)
                try:
                    bashCommand = "touch {}".format(fname)
                    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
                    output, error = process.communicate()
                except:
                    pass
                i += 1 # for single shot loop execution
            try:
                # read the present file and add it to memory
                f_open = open(file, "r")
                content.append(f_open.read())
            except:
                pass

        print(fname + " has been created!")

        # parse the file content
        content = end_line.join(content)
        content = content.replace("-[x]","\n\n- [x]")
        content = content.replace("-[]","\n\n-")

        # dump file content from memory to summary file
        f_summary = open(fname, "a")
        title = actual_file.split(".")[0].capitalize()
        header = "---\ntitle: {}\nauthor: {}\ndate: {}\ngeometry: margin=2cm\n---\n".format(title,__author__,today.replace("_","-"))
        f_summary.write(header)
        f_summary.write(content)
        f_summary.close()

        #make pdf from markdown
        try:
            pdfname = fname.split(".")[0] + ".pdf"
            bashCommand = "pandoc -s -o {} {}".format(pdfname,fname)
            process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        except:
            pass
        print(pdfname + " has been created!")



if __name__ == "__main__":
    project_root = "/Users/shanto/LFL/Summer22"
    files = ["summary.md","goals.md"]
    target_path = "/Users/shanto/LFL/Meetings/meeting_materials/summaries_of_the_week"

    all_paths = get_all_paths(project_root)
    all_files = get_all_files(all_paths, files)
    create_file_dump(all_files, target_path)
