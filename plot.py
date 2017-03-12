"""
This is a script for course project in CMPS263, UCSC 2017 Winter.
We generate graphs using pygal, potly libraries.

Author:
Yanzhong Li     yli185@ucsc.edu

"""

import csv
import sys
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import *
import pandas as pd
import pygal
import plotly.graph_objs as go
from pygal.style import Style
from pygal.style import DarkenStyle
darken_style = DarkenStyle('#ff8723', step = 20)

US_STATES = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
US_STATE_SHORT_dic = {'WA': 'Washington', 'DE': 'Delaware', 'WI': 'Wisconsin', 'WV': 'West Virginia', 'HI': 'Hawaii', 'FL': 'Florida', 'WY': 'Wyoming', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'TX': 'Texas', 'LA': 'Louisiana', 'NC': 'North Carolina', 'ND': 'North Dakota', 'NE': 'Nebraska', 'TN': 'Tennessee', 'NY': 'New York', 'PA': 'Pennsylvania', 'CA': 'California', 'NV': 'Nevada', 'VA': 'Virginia', 'CO': 'Colorado', 'AK': 'Alaska', 'AL': 'Alabama', 'AR': 'Arkansas', 'VT': 'Vermont', 'IL': 'Illinois', 'GA': 'Georgia', 'IN': 'Indiana', 'IA': 'Iowa', 'OK': 'Oklahoma', 'AZ': 'Arizona', 'ID': 'Idaho', 'CT': 'Connecticut', 'ME': 'Maine', 'MD': 'Maryland', 'MA': 'Massachusetts', 'OH': 'Ohio', 'UT': 'Utah', 'MO': 'Missouri', 'MN': 'Minnesota', 'MI': 'Michigan', 'RI': 'Rhode Island', 'KS': 'Kansas', 'MT': 'Montana', 'MS': 'Mississippi', 'SC': 'South Carolina', 'KY': 'Kentucky', 'OR': 'Oregon', 'SD': 'South Dakota'}


def plotPermChoropleth (dataFilePath, outputPath):
    df = pd.read_csv(dataFilePath)
    for col in df.columns:
        df[col] = df[col].astype(str)
    scl = [[0.0, 'rgb(242,240,247)'],[0.02, 'rgb(218,218,235)'],[0.03, 'rgb(188,189,220)'],\
                [0.05, 'rgb(158,154,200)'],[0.08, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]
    df['text'] = df['FullStateName'] + '<br>' +\
                'Total Applicants: ' + df['applicants_count']
    data = [ dict(
            type='choropleth',
            hoverinfo = "text",
            colorscale = scl,
            autocolorscale = True,
            locations = df['State'],
            z = df['applicants_count'].astype(float),
            locationmode = 'USA-states',
            text = df['text'],
            marker = dict(
                line = dict (
                    color = 'rgb(255,255,255)',
                    width = 2
                ) ),
            showscale = True,
            colorbar = dict(
                    thicknessmode = "pixels",
                    thickness = 10,
                    lenmode = "pixels",
                    len = 300
                )
            ) ]
    layout = dict(
            title = '<br>2016 EB-2/EB-3 Applicants by State',
            geo = dict(
                scope='usa',
                projection=dict( type='albers usa' ),
                showlakes = True,
                lakecolor = 'rgb(255, 255, 255)'),
            margin = go.Margin(
                        l=0,
                        r=0,
                        b=0,
                        t=0,
                        pad=0
                    )
                 )
    fig = dict( data=data, layout=layout )
    # py.iplot( fig, filename='d3-cloropleth-map' )
    plot(fig, filename = outputPath)
    # plotly.offline.plot(data, filename = 'basic-line.html')


def plotPermBarCharts (dataFilePath, outputPath) :
    for short_name in US_STATES:
        with open(dataFilePath + short_name + '.csv', 'rb') as csvfile:
            stateData = list(csv.reader(csvfile))
        custom_style = Style(
              tooltip_font_size = 18,
              legend_font_size = 13,
              value_font_size = 15,
              title_font_size = 18
              )
        bar_chart = pygal.HorizontalBar(
                legend_box_size = 10,
                hieght = 100,
                style = custom_style,
                print_values = True,
                margin = 20
                )
        bar_chart.title = 'Top 30 foreign-worker-friendly Companies in ' + US_STATE_SHORT_dic[short_name]
        topX = 20
        if (short_name == 'MO'):
            topX = 17
        for row in stateData[1:topX+1]:
            bar_chart.add(str(row[0]), float(row[1]), rounded_bars = 3)
        # bar_chart.render_in_browser()
        bar_chart.render_to_file(outputPath + short_name + '.svg')

if __name__ == "__main__":

    if (len(sys.argv) > 1):
        if (sys.argv[1] == "perm"):
            plotPermChoropleth('./output/viz/PERM_Companies/_PERM_StateByCase.csv', './output/viz/PERM_Companies/_PERM_Choropleth.html')
            plotPermBarCharts('./output/viz/PERM_Companies/', './output/viz/PERM_Companies/svg/')
        elif (sys.argv[1] == "h1b"):
            plotPermChoropleth('./output/viz/H1B_Companies/state_count_workers.csv', './output/viz/H1B_Companies/_H1B_Choropleth.html')
            plotPermBarCharts('./output/viz/H1B_Companies/', './output/viz/H1B_Companies/svg/')












pass
