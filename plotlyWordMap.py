

import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

import plotly.plotly as py
import pandas as pd

df = pd.read_csv('./output/viz/PERM_Peers/ctryAbbr_count_Plotly.csv')
# abbrCountryName   count
data = [ dict(
        type = 'choropleth',
        locations = df['abbr'],
        z = df['count'],
        text = df['countryName'],
        colorscale = [[0,"rgb(5, 10, 172)"],[0.15,"rgb(40, 60, 190)"],[0.3,"rgb(70, 100, 245)"],\
            [0.4,"rgb(90, 120, 245)"],[0.5,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"]],
        autocolorscale = True,
        reversescale = False,
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
        colorbar = dict(
            autotick = False,
            tickprefix = '$',
            title = 'GDP<br>Billions US$'),
      ) ]

layout = dict(
    title = 'Where are they from?',
    geo = dict(
        showframe = False,
        showcoastlines = False,
        projection = dict(
            type = 'Mercator'
        )
    )
)
fig = dict( data=data, layout=layout )
plot( fig, validate=False, filename='./output/viz/PERM_Peers/whereTheyFrom.html' )
# fig = dict( data=data, layout=layout )
# # py.iplot( fig, filename='d3-cloropleth-map' )
# plot(fig, filename = outputPath)
# # plotly.offline.plot(data, filename = 'basic-line.html')
