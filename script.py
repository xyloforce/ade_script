#!/usr/bin/env python3
import icalendar
import requests
import sys
import re

# create object from file
url="http://adelb.univ-lyon1.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?resources=9020,33894,10107,62768&projectId=2&calType=ical&firstDate=2020-09-07&lastDate=2021-01-01" # change it
dl=requests.get(url)
open('/tmp/cal.ics', 'wb').write(dl.content)
calendar_file=open("/tmp/cal.ics")
calendar=icalendar.Calendar.from_ical(calendar_file.read())
calendar_file.close()
# create new calendar to save valid events
calendar_corrected=icalendar.Calendar()
calendar_corrected.add('prodid', '-//My calendar product//mxm.dk//')
calendar_corrected.add('version', '2.0')

# walk through the calendar and get events as components
for component in calendar.walk():
    if component.name=="VEVENT":
        # if event has summary corresponding to a valid UE
        if re.search("DCD|Graphes|Introduction", component.get('summary')): # change according to your UE
            calendar_corrected.add_component(component)
        # else if it is a M2BI UE
        elif re.search("M2BI", component.get('description')): # do not change if you're a M2BI student
            calendar_corrected.add_component(component)
            
# save to file
ccorrected_file=open("/home/fabien/Documents/Cours/3_M2/calendar_correct.ics", 'wb') # adapt the path
ccorrected_file.write(calendar_corrected.to_ical())
ccorrected_file.close()
