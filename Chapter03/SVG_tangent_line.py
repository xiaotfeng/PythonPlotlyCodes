
import plotly as py
import plotly.graph_objs as go
import numpy as np

# ----------pre def
pyplt = py.offline.plot

x0 = np.linspace(1, 3, 200)
y0 = x0 * np.sin(np.power(x0, 2)) + 1

trace0 = go.Scatter(
    x=x0,
    y=y0,
)
data = [trace0]
layout = {
    'title': "f(x)=sin(x^2)+1",
    'shapes': [
        {
            'type': 'line',
            'x0': 1,
            'y0': 2.30756,
            'x1': 1.75,
            'y1': 2.30756,
            'opacity': 0.7,
            'line': {
                'color': 'red',
                'width': 2.5,
            },
        },
        {
            'type': 'line',
            'x0': 2.5,
            'y0': 3.80796,
            'x1': 3.05,
            'y1': 3.80796,
            'opacity': 0.7,
            'line': {
                'color': 'red',
                'width': 2.5,
            },
        },
        {
            'type': 'line',
            'x0': 1.90,
            'y0': -1.1827,
            'x1': 2.50,
            'y1': -1.1827,
            'opacity': 0.7,
            'line': {
                'color': 'red',
                'width': 2.5,
            },
        },
    ]
}
fig = {
    'data': data,
    'layout': layout,
}
pyplt(fig, filename='tmp/tangent-line.html')