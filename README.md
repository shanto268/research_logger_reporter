# Requirements

- have `python` installed on your machine

- have `pandoc` installed on your machine (*just `brew install pandoc`*)

# Purpose

1. Creates directory based on the day for tracking research progress (i.e. goals, summary and any work done). 
2. Creates a **summary pdf** based on all the markdown logs (an accumulation of) you have made each week at a certain time/day (i.e. change to sometime before your 1 to 1 meetings etc)

# Configuration

## For Work Logging:

1. **Update the `workLogger.py` code**: 
  - Change the project root file directory (i.e. `project_root` variable)
  - add any more files to be auto-generated (i.e. `files` variable)

2. **Update the `LFLworkLogger-launchd` file:**
  - rename the file to be more descriptive of your requirements
  - update the path to `python` binary
  - update the `text, title` variables to meet your alert needs


3. **Update the `com.shanto.LFLworkLogger.plist` file:**
  - rename the file to be more descriptive of your requirements
    - make sure the new name is reflected on the `<string>` tag for the `Label <key>`
  - update the path to the launchd file (i.e. `<string> for the Program <key>`)
  - update all the `Standard*Paths`
  - update the path to the code/local repo clone(i.e. `<string>` of `WorkingDirectory <key>`)
  - update the time when you want the daemon service to launch (*I have it set as 8 AM in the code*)
  - move the `plist` file to the `~/Library/LaunchAgents/` directory (create it if not already there)


## For Summary Reporting:

1. **Update the `createWeekSummaryReport.py` code**: 
  - Change the following variables to match your needs
    ```
    project_root = "/Users/shanto/LFL/Summer22"
    files = ["summary.md","goals.md"]
    target_path = "/Users/shanto/LFL/Meetings/meeting_materials/summaries_of_the_week"
    ```


2. **Update the `LFLsummaryReporter-launchd` file:**
  - rename the file to be more descriptive of your requirements
  - update the path to `python` binary
  - update the `text, title` variables to meet your alert needs


3. **Update the `com.shanto.LFLsummaryReporter.plist` file:**
  - rename the file to be more descriptive of your requirements
    - make sure the new name is reflected on the `<string>` tag for the `Label <key>`
  - update the path to the launchd file (i.e. `<string> for the Program <key>`)
  - update all the `Standard*Paths`
  - update the path to the code/local repo clone(i.e. `<string>` of `WorkingDirectory <key>`)
  - update the time when you want the daemon service to launch (*mine is Tuesday 12 PM*) [**Weekday 7 == Sunday** and **Weekday 0 == Saturday**]

    ```
    <key>StartCalendarInterval</key>
        <dict>
            <key>Weekday</key>
            <integer>2</integer>
            <key>Hour</key>
            <integer>12</integer>
            <key>Minute</key>
            <integer>0</integer>
        </dict>
      ```

  - move the `plist` file to the `~/Library/LaunchAgents/` directory (create it if not already there)


# Usage

First test the code works as intended by running the `launchd` bash script. If it works well, then start the daemon process by 

```
$ cp *.plist ~/Library/LaunchAgents
$ cd ~/Library/LaunchAgents #create this directory if missing
$ launchctl load -w nameOfWorkLoggerPlistFile.plist 
$ launchctl load -w nameOfSummaryReporterPlistFile.plist
```

# Functionality Request:

-[  ] Autoformatting of links in summary files
-[  ] Don't include files where no work is done in the summary pdf (e.g. some weekends or holidays)
-[  ] Automoving of unfinished goals to the next day for `workLogger.py`
-[  ] Allow latex formula
-[  ] Create functionality for creating summary pdf corresponding to each `# tags` in the `.md` files


# Disclaimers

- **OF COURSE WORK LOGGER FUNCTIONALITY CAN BE USED WITHOUTH SUMMARY REPORTING**
- **WORKS ONLY FOR MAC OS. CAN BE EASILY CHANGED FOR LINUX BY USING CRON INSTEAD OF LAUNCHD**
