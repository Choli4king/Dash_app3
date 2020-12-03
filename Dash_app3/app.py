
import dash
#from dash import Dash
import dash_bootstrap_components as dbc
from flask_caching import Cache

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__,suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])


app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP], # switch BOOTSTRAP for SOLAR
                meta_tags=[{'name': 'viewport',
                            'content':'width=device-width, initial-scale=1.0'}]
)
cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})
server = app.server