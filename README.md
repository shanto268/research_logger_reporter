**WORKS ONLY FOR MAC OS. CAN BE EASILY CHANGED FOR LINUX BY USING CRON INSTEAD OF LAUNCHD**


# Purpose

Creates directory based on the day for tracking research progress (i.e. goals, summary and any work done)

# Configuration

1. **Update the python code**: 
  - Change the project root file directory (i.e. `project_root` variable)
  - add any more files to be auto-generated (i.e. `files` variable)

2. **Uupdate the `launchd` file:**
  - rename the file to be more descriptive of your requirements
  - update the path to `python` binary
  - update the `text, title` variables to meet your alert needs


3. **Uupdate the `plist` file:**
  - rename the file to be more descriptive of your requirements
    - make sure the new name is reflected on the `<string>` tag for the `Label <key>`
  - update the path to the launchd file (i.e. `<string> for the Program <key>`)
  - update all the `Standard*Paths`
  - update the path to the code/local repo clone(i.e. `<string>` of `WorkingDirectory <key>`)
  - update the time when you want the daemon service to launch (*I have it set as 8 AM in the code*)
  - move the `plist` file to the `~/Library/LaunchAgents/` directory (create it if not already there)

# Usage

First test the code works as intended by running the `launchd` bash script. If it works well, then start the daemon process by

`$ launchctl load -w nameOfPlistFile.plist #i.e. the .plist file in ~/Library/LaunchAgents/`
