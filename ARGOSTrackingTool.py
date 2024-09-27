#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: John Fay (john.fay@duke.edu)
# Date:   Fall 2024
#--------------------------------------------------------------

#Create a variable pointing to the data file
file_name = './data/raw/sara.txt'

#Create a file object from the file
file_object = open(file_name,'r')

#Read contents of file into a list
lineString = file_object.readline()

#Making a loop to iterate through ALL lines of the sara.txt ONE at a time (better to use with large data sets)
while lineString: #as long as reading line reutrns something, the loop will continue
    #Check if line is a data line
    if lineString[0] in ("#","u"): #if line starts with a # or u, then skip it and go to next
        lineString = file_object.readline() # Get the next item BEFORE it continues so we don't get stuck in a loop
        continue

    #Split the string into a list of data items
    lineData = lineString.split()

    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]

    #Print the location of sara
    print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")

    #Read next line (this also ensures the loop doesn't get stuck, and so it ends when this returns empty)
    lineString = file_object.readline()