#TAKES RAW DATA FROM BORIS AND FORMATS IT INTO WHAT WE WANT FOR THE SAMPSON DATA SHEET

import csv, math
from datetime import datetime
                        
                        #REPLACE WITH PROPER FILE NAME
with open('/Users/lydiayu/Dropbox (MIT)/UROP/D2_S2.csv', 'r') as data:
    content = csv.reader(data)
    rows = [row for row in content]
    data = rows[17:]

#create a list of all of the start/stop occurrences of music and use that to build the music rows
music = []
for x in range(0,len(data)):
    if data[x][5].lower() == 'music':
        music.append(data[x])

#list of information for each row of music data, a mock csv file
musicData = []
for i in range(0,len(music),2):
        letter = activities.get(music[i][5].lower())
        activityType = music[i][6]
        visitors = rows[14][1]
        musicVal = 'YES'
        timeStart = str(math.floor(float(music[i][0])/60)).zfill(2) + ":" + \
            str(int(round((float(music[i][0])/60-
                    math.floor(float(music[i][0])/60))*60))).zfill(2)
        timeEnd = str(math.floor(float(music[i+1][0])/60)).zfill(2) + ":" + \
                str(int(round((float(music[i+1][0])/60-
                            math.floor(float(music[i+1][0])/60))*60))).zfill(2)
        musicData.append([2, 2, letter, activityType, 
                                visitors, musicVal, timeStart, timeEnd])

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
            "feathers puffing":"FP",
            "music":"U"}

#adds rows to new csv file with with all other activities that aren't music
        #REPLACE WITH PROPER FILE NAME!!!!
with open('day2.2.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', 
                            quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Day', 'Session', 'Activity', 'Event or behavior?', 
                         'Visitors?','Music?','Time Start', 'Time End'])

    for x in range(0,len(data)):
        if data[x][5].lower() != 'music' and data[x][8] == 'START': 
            letter = activities.get(data[x][5].lower())
            activityType = data[x][6]
            visitors = rows[14][1]
            music = data[x][9]
            timeStart = str(math.floor(float(data[x][0])/60)).zfill(2) + ":" + \
                str(int(round((float(data[x][0])/60-
                            math.floor(float(data[x][0])/60))*60))).zfill(2)
            if data[x+1][5].lower() == data[x][5].lower() and data[x+1][8] == 'STOP':
                timeEnd = str(math.floor(float(data[x+1][0])/60)).zfill(2) + ":" + \
                    str(int(round((float(data[x+1][0])/60-
                                math.floor(float(data[x+1][0])/60))*60))).zfill(2)
            else:
                timeEnd = str(math.floor(float(data[x+2][0])/60)).zfill(2) + ":" + \
                    str(int(round((float(data[x+2][0])/60-
                            math.floor(float(data[x+2][0])/60))*60))).zfill(2)

                #REPLACE DAY AND SESSION WITH CORRECT NUMBERS!!!!
            filewriter.writerow([2, 2, letter, activityType, 
                            visitors, music, timeStart, timeEnd]) 
    #ADD MUSICDATA TO END OF CSV
    for line in musicData:
        filewriter.writerow(line)                            

    # sort csv by time start to put music in right location
fullCSV = csv.reader(open('day2.2.csv'))
sortedCSV = sorted(fullCSV, key=lambda x: x[6], reverse=False)
with open('day2.2.csv', 'w') as f:
    fileWriter = csv.writer(f, delimiter=',')
    fileWriter.writerow(sortedCSV[-1])
    for row in range(0, len(sortedCSV)-1):
              fileWriter.writerow(sortedCSV[row])
