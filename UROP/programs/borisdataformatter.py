#TAKES RAW DATA FROM BORIS AND FORMATS IT INTO WHAT WE WANT FOR THE SAMPSON DATA SHEET

import csv, math
from datetime import datetime
                        
                        #REPLACE WITH PROPER FILE NAME
with open('/Users/lydiayu/Dropbox (MIT)/UROP/Raw Data/d4s3.csv', 'r') as data:
    content = csv.reader(data)
    rows = [row for row in content]
    data = rows[17:]

#create a list of all of the start/stop occurrences of each type of activity
music, nodding, bobbing, vocalization, whisteling, moving, headWhips, pruning, stretching, eating, oneLeg, nibbling, feathersPuffing = ([] for i in range(13))
for x in range(0,len(data)):
    if data[x][5].lower() == 'music':
        music.append(data[x])
    elif data[x][5].lower() == 'nodding':
        nodding.append(data[x])
    elif data[x][5].lower() == 'bobbing':
        bobbing.append(data[x])
    elif data[x][5].lower() == 'vocalization':
        vocalization.append(data[x])
    elif data[x][5].lower() == 'whisteling':
        whisteling.append(data[x])
    elif data[x][5].lower() == 'moving':
        moving.append(data[x])
    elif data[x][5].lower() == 'head whips':
        headWhips.append(data[x])
    elif data[x][5].lower() == 'pruning':
        pruning.append(data[x])
    elif data[x][5].lower() == 'stretching':
        stretching.append(data[x])
    elif data[x][5].lower() == 'eating':
        eating.append(data[x])
    elif data[x][5].lower() == 'standing on one leg':
        oneLeg.append(data[x])
    elif data[x][5].lower() == 'nibbling':
        nibbling.append(data[x])
    else:
        feathersPuffing.append(data[x])

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

musicData, noddingData, bobbingData, vocalizationData, whistelingData, movingData, headWhipsData, pruningData, stretchingData, eatingData, oneLegData, nibblingData, feathersPuffingData = ([] for i in range(13))

#list of information for each row of data
for i in range(0,len(music),2):
        letter = activities.get(music[i][5].lower())
        activityType = music[i][6]
        visitors = rows[14][1]
        musicVal = data[1][9]
        timeStart = str(math.floor(float(music[i][0])/60)).zfill(2) + ":" + \
            str(int(round((float(music[i][0])/60-
                    math.floor(float(music[i][0])/60))*60))).zfill(2)
        timeEnd = str(math.floor(float(music[i+1][0])/60)).zfill(2) + ":" + \
                str(int(round((float(music[i+1][0])/60-
                            math.floor(float(music[i+1][0])/60))*60))).zfill(2)
        musicData.append([2, 2, letter, activityType, 
                                visitors, musicVal, timeStart, timeEnd])
for i in range(0,len(nodding),2):
        letter = activities.get(nodding[i][5].lower())
        activityType = nodding[i][6]
        visitors = rows[14][1]
        musicVal = data[1][9]
        timeStart = str(math.floor(float(nodding[i][0])/60)).zfill(2) + ":" + \
            str(int(round((float(nodding[i][0])/60-
                    math.floor(float(nodding[i][0])/60))*60))).zfill(2)
        timeEnd = str(math.floor(float(nodding[i+1][0])/60)).zfill(2) + ":" + \
                str(int(round((float(nodding[i+1][0])/60-
                            math.floor(float(nodding[i+1][0])/60))*60))).zfill(2)
        noddingData.append([2, 2, letter, activityType, 
                                visitors, musicVal, timeStart, timeEnd])
for i in range(0,len(bobbing),2):
        letter = activities.get(bobbing[i][5].lower())
        activityType = bobbing[i][6]
        visitors = rows[14][1]
        musicVal = data[1][9]
        timeStart = str(math.floor(float(bobbing[i][0])/60)).zfill(2) + ":" + \
            str(int(round((float(bobbing[i][0])/60-
                    math.floor(float(bobbing[i][0])/60))*60))).zfill(2)
        timeEnd = str(math.floor(float(bobbing[i+1][0])/60)).zfill(2) + ":" + \
                str(int(round((float(bobbing[i+1][0])/60-
                            math.floor(float(bobbing[i+1][0])/60))*60))).zfill(2)
        bobbingData.append([2, 2, letter, activityType, 
                                visitors, musicVal, timeStart, timeEnd])
for i in range(0,len(vocalization),2):
        letter = activities.get(vocalization[i][5].lower())
        activityType = vocalization[i][6]
        visitors = rows[14][1]
        musicVal = data[1][9]
        timeStart = str(math.floor(float(vocalization[i][0])/60)).zfill(2) + ":" + \
            str(int(round((float(vocalization[i][0])/60-
                    math.floor(float(vocalization[i][0])/60))*60))).zfill(2)
        timeEnd = str(math.floor(float(vocalization[i+1][0])/60)).zfill(2) + ":" + \
                str(int(round((float(vocalization[i+1][0])/60-
                            math.floor(float(vocalization[i+1][0])/60))*60))).zfill(2)
        vocalizationData.append([2, 2, letter, activityType, 
                                visitors, musicVal, timeStart, timeEnd])
for i in range(0,len(whisteling),2):
        letter = activities.get(whisteling[i][5].lower())
        activityType = whisteling[i][6]
        visitors = rows[14][1]
        musicVal = data[1][9]
        timeStart = str(math.floor(float(whisteling[i][0])/60)).zfill(2) + ":" + \
            str(int(round((float(whisteling[i][0])/60-
                    math.floor(float(whisteling[i][0])/60))*60))).zfill(2)
        timeEnd = str(math.floor(float(whisteling[i+1][0])/60)).zfill(2) + ":" + \
                str(int(round((float(whisteling[i+1][0])/60-
                            math.floor(float(whisteling[i+1][0])/60))*60))).zfill(2)
        whistelingData.append([2, 2, letter, activityType, 
                                visitors, musicVal, timeStart, timeEnd])
for i in range(0,len(moving),2):
        letter = activities.get(moving[i][5].lower())
        activityType = moving[i][6]
        visitors = rows[14][1]
        musicVal = data[1][9]
        timeStart = str(math.floor(float(moving[i][0])/60)).zfill(2) + ":" + \
            str(int(round((float(moving[i][0])/60-
                    math.floor(float(moving[i][0])/60))*60))).zfill(2)
        timeEnd = str(math.floor(float(moving[i+1][0])/60)).zfill(2) + ":" + \
                str(int(round((float(moving[i+1][0])/60-
                            math.floor(float(moving[i+1][0])/60))*60))).zfill(2)
        movingData.append([2, 2, letter, activityType, 
                                visitors, musicVal, timeStart, timeEnd])
for i in range(0,len(headWhips),2):
        letter = activities.get(headWhips[i][5].lower())
        activityType = headWhips[i][6]
        visitors = rows[14][1]
        musicVal = data[1][9]
        timeStart = str(math.floor(float(headWhips[i][0])/60)).zfill(2) + ":" + \
            str(int(round((float(headWhips[i][0])/60-
                    math.floor(float(headWhips[i][0])/60))*60))).zfill(2)
        timeEnd = str(math.floor(float(headWhips[i+1][0])/60)).zfill(2) + ":" + \
                str(int(round((float(headWhips[i+1][0])/60-
                            math.floor(float(headWhips[i+1][0])/60))*60))).zfill(2)
        headWhipsData.append([2, 2, letter, activityType, 
                                visitors, musicVal, timeStart, timeEnd])
for i in range(0,len(pruning),2):
        letter = activities.get(pruning[i][5].lower())
        activityType = pruning[i][6]
        visitors = rows[14][1]
        musicVal = data[1][9]
        timeStart = str(math.floor(float(pruning[i][0])/60)).zfill(2) + ":" + \
            str(int(round((float(pruning[i][0])/60-
                    math.floor(float(pruning[i][0])/60))*60))).zfill(2)
        timeEnd = str(math.floor(float(pruning[i+1][0])/60)).zfill(2) + ":" + \
                str(int(round((float(pruning[i+1][0])/60-
                            math.floor(float(pruning[i+1][0])/60))*60))).zfill(2)
        pruningData.append([2, 2, letter, activityType, 
                                visitors, musicVal, timeStart, timeEnd])
for i in range(0,len(stretching),2):
        letter = activities.get(stretching[i][5].lower())
        activityType = stretching[i][6]
        visitors = rows[14][1]
        musicVal = data[1][9]
        timeStart = str(math.floor(float(stretching[i][0])/60)).zfill(2) + ":" + \
            str(int(round((float(stretching[i][0])/60-
                    math.floor(float(stretching[i][0])/60))*60))).zfill(2)
        timeEnd = str(math.floor(float(stretching[i+1][0])/60)).zfill(2) + ":" + \
                str(int(round((float(stretching[i+1][0])/60-
                            math.floor(float(stretching[i+1][0])/60))*60))).zfill(2)
        stretchingData.append([2, 2, letter, activityType, 
                                visitors, musicVal, timeStart, timeEnd])
for i in range(0,len(eating),2):
        letter = activities.get(eating[i][5].lower())
        activityType = eating[i][6]
        visitors = rows[14][1]
        musicVal = data[1][9]
        timeStart = str(math.floor(float(eating[i][0])/60)).zfill(2) + ":" + \
            str(int(round((float(eating[i][0])/60-
                    math.floor(float(eating[i][0])/60))*60))).zfill(2)
        timeEnd = str(math.floor(float(eating[i+1][0])/60)).zfill(2) + ":" + \
                str(int(round((float(eating[i+1][0])/60-
                            math.floor(float(eating[i+1][0])/60))*60))).zfill(2)
        eatingData.append([2, 2, letter, activityType, 
                                visitors, musicVal, timeStart, timeEnd])
for i in range(0,len(oneLeg),2):
        letter = activities.get(oneLeg[i][5].lower())
        activityType = oneLeg[i][6]
        visitors = rows[14][1]
        musicVal = data[1][9]
        timeStart = str(math.floor(float(oneLeg[i][0])/60)).zfill(2) + ":" + \
            str(int(round((float(oneLeg[i][0])/60-
                    math.floor(float(oneLeg[i][0])/60))*60))).zfill(2)
        timeEnd = str(math.floor(float(oneLeg[i+1][0])/60)).zfill(2) + ":" + \
                str(int(round((float(oneLeg[i+1][0])/60-
                            math.floor(float(oneLeg[i+1][0])/60))*60))).zfill(2)
        oneLegData.append([2, 2, letter, activityType, 
                                visitors, musicVal, timeStart, timeEnd])
for i in range(0,len(nibbling),2):
        letter = activities.get(nibbling[i][5].lower())
        activityType = nibbling[i][6]
        visitors = rows[14][1]
        musicVal = data[1][9]
        timeStart = str(math.floor(float(nibbling[i][0])/60)).zfill(2) + ":" + \
            str(int(round((float(nibbling[i][0])/60-
                    math.floor(float(nibbling[i][0])/60))*60))).zfill(2)
        timeEnd = str(math.floor(float(nibbling[i+1][0])/60)).zfill(2) + ":" + \
                str(int(round((float(nibbling[i+1][0])/60-
                            math.floor(float(nibbling[i+1][0])/60))*60))).zfill(2)
        nibblingData.append([2, 2, letter, activityType, 
                                visitors, musicVal, timeStart, timeEnd])
for i in range(0,len(feathersPuffing),2):
        letter = activities.get(feathersPuffing[i][5].lower())
        activityType = feathersPuffing[i][6]
        visitors = rows[14][1]
        musicVal = data[1][9]
        timeStart = str(math.floor(float(feathersPuffing[i][0])/60)).zfill(2) + ":" + \
            str(int(round((float(feathersPuffing[i][0])/60-
                    math.floor(float(feathersPuffing[i][0])/60))*60))).zfill(2)
        timeEnd = str(math.floor(float(feathersPuffing[i+1][0])/60)).zfill(2) + ":" + \
                str(int(round((float(feathersPuffing[i+1][0])/60-
                            math.floor(float(feathersPuffing[i+1][0])/60))*60))).zfill(2)
        feathersPuffingData.append([2, 2, letter, activityType, 
                                visitors, musicVal, timeStart, timeEnd])

#create a list of lists of all of the activity data
allData = [musicData, noddingData, bobbingData, vocalizationData, whistelingData, movingData, headWhipsData, 
            pruningData, stretchingData, eatingData, oneLegData, nibblingData, feathersPuffingData]

#adds rows to new csv file with with all activities
with open('day4.3.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', 
                            quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Day', 'Session', 'Activity', 'Event or behavior?', 
                         'Visitors?','Music?','Time Start', 'Time End'])
    for dataList in allData:
        for line in dataList:
            filewriter.writerow(line)

 # sort csv by time start to put activities in right order
fullCSV = csv.reader(open('day4.3.csv'))
sortedCSV = sorted(fullCSV, key=lambda x: x[6], reverse=False)
with open('day4.3.csv', 'w') as f:
    fileWriter = csv.writer(f, delimiter=',')
    fileWriter.writerow(sortedCSV[-1])
    for row in range(0, len(sortedCSV)-1):
              fileWriter.writerow(sortedCSV[row]