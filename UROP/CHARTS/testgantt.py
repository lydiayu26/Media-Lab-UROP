import plotly.figure_factory as ff 
import pandas as pd 

#take in data, use only data from day 1:
data = pd.read_csv("/users/lydiayu/Dropbox (MIT)/UROP/SampsonACTIVITIES.csv")
day1 = data.loc[210:422,:]

activities = {"N":"nodding",
            "B":"bobbing",
            "V":"vocalization",
            "W":"whisteling",
            "M":"moving",
            "H":"head whips",
            "P":"pruning",
            "S":"stretching",
            "E":"eating",
            "L":"standing on one leg",
            "NB":"nibbling",
            "FP":"feathers puffing"}

#create a list of the start/end times of ALL the different Sampson activites
#df = []
"""
for index, row in day1.head().iterrows():
    act = activities.get(row['Activity'])
    activity = dict(Task = act, Start = row['Start'], Finish = row['End'], Resource = row['Activity'])
    df.append(activity)
"""
df = [dict(Task= 'moving', Start= '01:07:29', Finish= '01:07:32', Resource= 'M'),
dict(Task ='standing on one leg', Start= '01:07:32', Finish='01:07:46', Resource= 'L'),
dict(Task= 'moving', Start= '01:07:50', Finish= '01:07:55', Resource= 'M'),
dict(Task= 'stretching', Start= '01:08:07', Finish= '01:08:10', Resource= 'S'),
dict(Task= 'bobbing', Start= '01:08:11', Finish= '01:08:14', Resource= 'B')]

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

fig = ff.create_gantt(df, colors=colordict, index_col='Resource', title='Sampson Activities', show_colorbar=True, group_tasks=True)
fig['layout']['xaxis']['tickformat'] = '%H:%M:%S'
#fig['layout']['xaxis']['autotick'] = False
fig['layout']['xaxis']['range'] = (0, 7200000)
#fig['layout']['xaxis']['tick0'] = -57600000
fig['layout']['xaxis']['dtick'] = 600000
#fig['layout']['xaxis']['ticktext']  = list(range(len(fig['layout']['xaxis']['tickvals'])))
#fig.layout.xaxis.rangeselector = None
#fig.layout.xaxis.type = 'linear'
fig.show()