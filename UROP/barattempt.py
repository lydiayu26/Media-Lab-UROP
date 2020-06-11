import pandas as pd 
import plotly.graph_objs as go 

data = pd.read_csv("/users/lydiayu/Dropbox (MIT)/UROP/SampsonACTIVITIES.csv")
df = data.loc[210:422,:]
df['duration'] = df['EndSec'] - df['StartSec']

fig = go.Figure(layout = {
            'barmode': 'stack',
            'xaxis': {'automargin': True},
            'yaxis': {'automargin': True}})

for activity, activity_df in df.groupby('Activity'):
    fig.add_bar(x=activity_df.duration,
                y=activity_df.activity,
                base=character.df.Start,
                orientation='h')
                #name=activity)
fig.update_layout(showlegend = False)
fig.show()

