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

# Ask user for a date
user_date = input("Enter a date: ") #This creates a prompt for user to type in a date

#Create a variable pointing to the data file
file_name = './data/raw/sara.txt'

#Create a file object from the file
file_object = open(file_name,'r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

#Initialize dictionaries using {}
date_dict = {}
location_dict = {}

#Making a loop to iterate through ALL lines of the sara.txt
for lineString in line_list:
    #Check if lineis a data line
    if lineString[0] in ("#", "u"): #if line starts with a # or u, then skip it and go to next
        continue

    #Split the string into a list of data items
    lineData = lineString.split()

    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]

    # Determine if location class criteria is met
    if obs_lc in ("1","2","3"):
        #Add items to dictionaries if lc is met
        date_dict[record_id] = obs_date # using record_id as key, obs_date as value
        location_dict[record_id] = (obs_lat, obs_lon) # using record_id as key, and (lat,lon) as value

# Collect keys if date matches the user input date (OUT of loop!!)
keys = [] #Initialize EMPTY key list with empty []

# Loop through items in date_dict
for item in date_dict.items():
    key = item[0] # Keys are all the first items (record_id)
    value = item[1] # Values are the second items (date)
    if value == user_date: 
        keys.append(key) # If date in item matches input, THEN add to end of "keys" list from above

# Report if no records were found
if len(keys) == 0:
    print(f"No records were found on {user_date}")

#Loop through keys and report locations
for key in keys:
    location = location_dict[key] #save the location of record-ids
    lat = location[0] #get first value in location variable
    lon = location[1]
    print(f"On {user_date}, Sara the turtle was seen at {lat}d Lat, {lon}d Lng.")