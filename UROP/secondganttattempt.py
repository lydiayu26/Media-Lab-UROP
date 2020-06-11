import plotly.figure_factory as ff 
import pandas as pd 

#take in data, use only data from day 1:
data = pd.read_csv("/users/lydiayu/Dropbox (MIT)/UROP/SampsonACTIVITIES.csv")
#day1 = data.loc[210:422,:]

day1 = data.loc[210:260,:]

#create a list of the start/end times of ALL the different Sampson activites
df = []

for index, row in day1.head().iterrows():
    activity = dict(Task = row['Activity'], Start = "2019-04-09" + row['Start'], Finish = "2019-04-09" + row['End'], Resource = row['Activity'])
    df.append(activity)

#create dictionary for colors. Diff color for each activity in this case.
colordict = dict(N = 'rgb(220,20,60)',
            B = 'rgb(255,160,122)',
            V = 'rgb(255,215,0)',
            W = 'rgb(144,238,144)',
            M = 'rgb(32,178,170)',
            H = 'rgb(100,149,237)',
            P = 'rgb(135,206,250)',
            S = 'rgb(0,0,139)',
            E = 'rgb(138,43,226)',
            L = 'rgb(255,0,255)',
            NB = 'rgb(199,21,133)',
            FP = 'rgb(255,228,196)')

fig = ff.create_gantt(df, colors=colordict, index_col='Resource', title='Sampson Activities', show_colorbar=True, bar_width=1.5, group_tasks=True)
fig.show()
