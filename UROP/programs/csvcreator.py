#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 17:32:06 2019

@author: lydiayu
"""

import csv, math
                        #REPLACE WITH PROPER FILE NAME
with open('/Users/lydiayu/Dropbox (MIT)/UROP/2.1.12.csv', 'r') as data:
    content = csv.reader(data)
    rows = [row for row in content]
    data = rows[17:]

activities = {"nodding":"N",
            "bobbing":"B",
            "vocalization":"V",
            "whisteling":"W",
            "moving":"M",
            "head whips":"H",
            "pruning":"P",
            "stretching":"S",
            "eating":"E",
            "standing on one leg":"L",
            "nibbling":"NB",
            "feathers puffing":"FP"}

        #REPLACE WITH PROPER FILE NAME!!!!
with open('day2.1.12.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', 
                            quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Day', 'Session', 'Activity', 'Event or behavior?', 
                         'Visitors?','Music?','Time Start', 'Time End'])
    for x in range(0,len(data),2):

        letter = activities.get(data[x][5])
        activityType = data[x][6]
        visitors = rows[14][1]
        music = data[x][9]

        timeStart = str(math.floor(float(data[x][0])/60)) + ":" + \
            str(int(round((float(data[x][0])/60-
                           math.floor(float(data[x][0])/60))*60))).zfill(2)
        timeEnd = str(math.floor(float(data[x+1][0])/60)) + ":" + \
            str(int(round((float(data[x+1][0])/60-
                           math.floor(float(data[x+1][0])/60))*60))).zfill(2)
            
            #REPLACE DAY AND SESSION WITH CORRECT NUMBERS!!!!
        filewriter.writerow([2, 1.12, letter, activityType, 
                             visitors, music, timeStart, timeEnd])


        """
        if content[x][0] == "n" or content[x][0] == "b" or content[x][0] == "v" or content[x][0] == "w" or content[x][0] == "m" or content[x][0] == "h":
            activityType = "EVENT"
            letter = content[x][0].upper()
        elif content[x][0] == "i":
            activityType = "BEHAVIOR"
            letter = "NB"
        elif content[x][0] == "f":
            activityType = "BEHAVIOR"
            letter = "FP"
        else:
            activityType = "BEHAVIOR"  
            letter = content[x][0].upper() 
        """ 