#!/bin/python3

import plotly.offline as py
import plotly.graph_objs as go

trace = go.Bar(x=[2, 4, 6], y= [10, 12, 15])
data = [trace]
layout = go.Layout(title='A Simple Plot', width=800, height=640)
fig = go.Figure(data=data, layout=layout)
py.plot(fig, auto_open=False, filename='plotly-test.html',
             image='svg', image_filename='plotly-test')
# svg image will be generated as soon as plotly-test.html is opened in browser
