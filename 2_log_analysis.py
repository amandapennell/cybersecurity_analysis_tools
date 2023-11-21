# PART 2: LOG FILE ANALYSIS

# You will need to analyze the provided log file (part2.log).
# This file contains log entries from a Linux server over the course of a month.

# The log entries are structured as follows:
# Month Day H:M:S Level Component[ProcessID]: Content

# For example, the following log entry follows this format:
# The component is sshd(pam_unix)
# The content shows an authentication failure from remote host 218.188.2.4. 

# Jun 14 15:16:01 combo sshd(pam_unix)[19939]: authentication failure; rhost=218.188.2.4

# import necessary libraries and modules

import re
from datetime import datetime
import matplotlib.pyplot as plt
from collections import Counter

#2.1 Open the log ﬁle such that only a single line at a time is loaded into memory

with open("part2.log") as file: # open log file
  text = file.read()  # read file
  print(len(text)) # print length of file

def openLogFile(path): # open log file
    with open(path) as log_file: # open file
        for log_entry in log_file: # loop through each line of file
            yield log_entry        # make function act as a generator to read file line by line

#2.2 Parse the log ﬁle and record the ﬁelds highlighted above

def parseLogFile(log_entry): # parse log file
    log_data = log_entry.strip().split() # split log entry into list of strings
    print(log_data) 
    r = {} # create dictionary to store log entry
    r["date"] = log_data[0:3] 
    r["level"] = log_data[3]  
    r["component"] = log_data[4] 
    r["message"] = log_data[5:] 
    return r 

logFile = openLogFile("part2.log") # open log file
print("First line of log file:") 
print(next(logFile)+"\n") #print first line of log file
entry = next(logFile) # store first line of log file
r = parseLogFile(entry) # parse first line of log file
print("Parsed first line of Log file:")
print(r)

# 2.3 Create a datetime object to record the date

date_string = "Jun 14 15:16:01" # date string
date_object = datetime.strptime(date_string, "%b %d %H:%M:%S") # create datetime object
print("datetime:")
print(date_object.strftime("%b %d %H:%M:%S")) 

# 2.4 Find and print the three most commonly used components.

def extract_component(log_entry): # extract component from log entry
    log_data = log_entry.strip().split() # split log entry into list of strings
    component = re.split(r'[^a-zA-Z]', log_data[4])[0] # regex to split component from log entry
    if component:
        return component 
    else:
        return None

with open("part2.log") as file: # open file
    components = [] # create list to store components
    for line in file: # iterate through each line of file
        component = extract_component(line) 
        if component:
            components.append(component) 

component_counts = Counter(components) # count occurrences of each component
print("Three most common components:")
for component, count in component_counts.most_common(3): # print 3 most common components
    print(component, count)

# 2.5 Brieﬂy describe these components as a comment.

# 1. ftpd: This is the daemon (utility program) responsible for handling incoming FTP connections.
#          It uses the TCP protocol and listens at the specified port.
# 2. sshd: This is the daemon responsible for handling incoming SSH connections.
#          It uses the TCP protocol and listens at the specified port.
# 3. su:   This is a Unix command used to switch to another user during a login session.
#          Most commonly used to change ownership from an ordinary user to the root user. 

# 2.6 Create a plot that shows how these three common components were used throughout the day. 
#     Divide the day into 2 periods (working hours and after hours).
#     Plot the number of entries for each component during those periods. 
#     Working hours are between 9 and 5.

def extract_hour(log_entry): # extract hour from log entry
    log_data = log_entry.strip().split() 
    date_string = " ".join(log_data[:3]) # combine into a single string
    date_object = datetime.strptime(date_string, "%b %d %H:%M:%S") # create datetime object
    return date_object.hour

def working_hours(log_entry): # check if log entry occurred during working hours
    hour = extract_hour(log_entry)
    return hour >= 9 and hour <= 17 # changed to military time

with open("part2.log") as file: # count occurrences of each component during working hours/after hours
    working_hours_counts = Counter() # create counter to store counts
    after_hours_counts = Counter()
    for line in file: # iterate through each line of file
        component = extract_component(line)
        if component:
            if working_hours(line):
                working_hours_counts[component] += 1 # increment count for component
            else:
                after_hours_counts[component] += 1 # increment count for component

components = [component for component, count in component_counts.most_common(3)] # get tuple of 3 most common components

# get counts for each component during working hours/after hours
working_hours_data = [working_hours_counts[component] for component in components] 
after_hours_data = [after_hours_counts[component] for component in components]

# plot results
plt.bar(components, working_hours_data, color="green", label="Working Hours")
plt.bar(components, after_hours_data, bottom=working_hours_data, color="black", label="After Hours")
plt.legend()
plt.xlabel("Component")
plt.ylabel("Number of Entries")
plt.title("Component Usage (Working Hours & After Hours)")
plt.show()

# a lot of activity after working hours!!!!