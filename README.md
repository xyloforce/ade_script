# ade_script
Script made to fix ICS files from Lyon 1 ADE.
## Use
1. clone the dir
2. install icalendar module (`pip3 install icalendar`) (ensure that the path is properly set)
2. change in script.py the URL for the ADE ics file, the UEs you have (it's a regex so check your file to ensure you don't get unexepected matches) and the save path
3. set your script to be launched upon start
4. import in Thunderbird/Lightning using new cal -> on the network -> set the path and prefix it using "file://"
