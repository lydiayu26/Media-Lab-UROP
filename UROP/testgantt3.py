import matplotlib.pyplot as plt 
import pandas as pd 

data = pd.read_csv("/users/lydiayu/Dropbox (MIT)/UROP/SampsonACTIVITIES.csv")
day1 = data.loc[210:422,:]

fig, gnt = plt.subplots()
gnt.set_ylim(0,120)
gnt.set_xlim(4000,30000)
gnt.set_xlabel('seconds since 1st vid start')
gnt.set_ylabel('Activity')

gnt.set_yticks([30, 60, 90])
gnt.set_yticklabels(['B','NB','M'])
gnt.grid(True)

y_pos = {"B": (20,30),
"NB": (50,60),
"M": (80,90)}

colors = {
    "B": 'tab:orange',
    "NB": 'tab:blue',
    "M": 'tab:red'
}

for index, row in day1.iterrows():
    #gnt.broken_barh([(40, 50)], (30, 9), facecolors =('tab:orange')) 
    if row['Activity'] == "B" or row['Activity'] == "NB" or row["Activity"]== "M":
        gnt.broken_barh([(row['StartSec'], row['EndSec'])], y_pos.get(row['Activity']), facecolors=colors.get(row['Activity']))

plt.savefig('gantt.png')