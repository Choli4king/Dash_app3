# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


#from app import app

# colors = {
#     'background': '#111111',
#     'text': '#8E3DEB'
# }

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
#

# df can be used to get all/any columns from original csv


'''
bar.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
),

pie.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
),
'''

#

layout = html.Div(id='charts')