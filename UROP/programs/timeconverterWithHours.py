#ADDS AN "HOUR" IN THE HOURS SLOT ON THE TIME THAT REPRESENTS THE VIDEO NUMBER. USED FOR GANTT CHART PURPOSES

import pandas as pd 
import math 

data = pd.read_csv("/users/lydiayu/Dropbox (MIT)/UROP/Sampson Data - ACTIVITIES.csv", header=0, usecols=[i for i in range(9)])

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
data.head()
data.to_csv("/users/lydiayu/Dropbox (MIT)/UROP/SampsonACTIVITIES.csv")