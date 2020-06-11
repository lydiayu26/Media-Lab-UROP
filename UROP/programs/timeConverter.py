#CONVERTS TIMING TO CORRECT FORMAT OR TO SECONDS

import pandas as pd
import math

#data = pd.read_csv("/users/lydiayu/Dropbox (MIT)/UROP/Sampson Data - ACTIVITIES-SESSIONS 2_3 WITH INT.csv", 
                  #header=11, usecols=[i for i in range(9)])
rawData = pd.read_csv("/users/lydiayu/Dropbox (MIT)/UROP/raw data/day4.3.csv")

def timeFormat(data):
    #create a list of new times that are in the correct format
    newStart = []
    for time in data['Time Start']:
        if len(time) == 4:
            start = '00:0' + time[0] + ':' + time[2:]
        #elif len(time) == 7:
        #    start = '00:' + time[2:4] + ':' + time[5:]
        elif len(time) == 7:
           start = '00:0' + time[0] + ':' + time[2:4]
        else:
            start = '00:' + time[0:2] + ':' + time[3:5]
        newStart.append(start)

    newEnd = []
    for time in data['Time End']:
        if len(time) == 4:
            end = '00:0' + time[0] + ':' + time[2:]
        #elif len(time) == 7:
        #    end = '00:' + time[2:4] + ':' + time[5:]
        elif len(time) == 7:
           end = '00:0' + time[0] + ':' + time[2:4]
        else:
            end = '00:' + time[0:2] + ':' + time[3:5]
        newEnd.append(end)

    #add the new times as new columns in the dataframe
    data['Start'] = newStart
    data['End'] = newEnd

    return data.to_csv("/users/lydiayu/Dropbox (MIT)/UROP/raw data/day4.3.csv")

def timeFormatWithHours(data):
    #create a list of new times that are in the correct format
    newStart = []
    for idx in range(len(data['Time Start'])):
        vidnum = str(data['Session'][idx])[2:].zfill(2)
        time = data['Time Start'][idx]
        if len(time) == 4:
            start = vidnum + ':0' + time[0] + ':' + time[2:]
        elif len(time) == 7:
            start = vidnum + ':' + time[2:4] + ':' + time[5:]
        else:
            start = vidnum + ':' + time[0:2] + ':' + time[3:5]

        newStart.append(start)

    newEnd = []
    for idx in range(len(data['Time End'])):
        vidnum = str(data['Session'][idx])[2:].zfill(2)
        time = data['Time End'][idx]
        if len(time) == 4:
            end = vidnum + ':0' + time[0] + ':' + time[2:]
        elif len(time) == 7:
            end = vidnum + ':' + time[2:4] + ':' + time[5:]
        else:
            end = vidnum + ':' + time[0:2] + ':' + time[3:5]

        newEnd.append(end)

    #add the new times as new columns in the dataframe
    data['Start'] = newStart
    data['End'] = newEnd
    data.to_csv("/users/lydiayu/Dropbox (MIT)/UROP/SampsonACTIVITIES.csv")

def addTimeSec(data):
    newStart = []
    for idx in range(len(data['Start'])):
        time = data['Start'][idx]
        if len(time) == 7:
            startSec = 3600*int(time[0]) + 60*int(time[2:4]) + int(time[5:])
        else:
            startSec = 3600*int(time[0:2]) + 60*int(time[3:5]) + int(time[6:])
        newStart.append(startSec)

    newEnd = []
    for idx in range(len(data['End'])):
        time = data['End'][idx]
        if len(time) == 7:
            endSec = 3600*int(time[0]) + 60*int(time[2:4]) + int(time[5:])
        else:
            endSec = 3600*int(time[0:2]) + 60*int(time[3:5]) + int(time[6:])
        newEnd.append(endSec)

    data['StartSec'] = newStart
    data['EndSec'] = newEnd
    data.to_csv("/users/lydiayu/Dropbox (MIT)/UROP/SampsonACTIVITIES.csv")
