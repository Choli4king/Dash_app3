
import base64
import datetime
import io

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.exceptions import PreventUpdate
from flask_caching import Cache
import plotly.express as px
import pandas as pd
import json
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.CardFooter import CardFooter
from dash_bootstrap_components._components.CardHeader import CardHeader
from dash_bootstrap_components._components.Col import Col

from apps import clean_div as cd, store_csv_in_div_cache as scc, charts, navbar, card_modal

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# cache = Cache(app.server, config={
#     'CACHE_TYPE': 'filesystem',
#     'CACHE_DIR': 'cache-directory'
# })

from app import app, cache, server
server = app.server

# static layout
app.layout = html.Div([
    html.Div([
        #html.Div(session_id, id='session-id', style={'display': 'none'}),
        #dcc.Store(id='store', storage_type='session'),
        html.Div(
            id='div-data', style={'display': 'none'}
        ),
        html.Div([
            navbar.layout
        ], className="Row"),
        html.Div([
            dcc.Location(id='url', refresh=False), # the unseen 'pathname' variable in this line for dcc is empty by default
            html.Div(id='page-content', children=[])
        ], className='Row'),
        
    ])
])



# toggle pages callback--------------------------------------------------------------------------------
@app.callback(Output(component_id='page-content', component_property='children'),
            [Input(component_id='url', component_property='pathname')], # we use pathname because it stores the last href
)
def display_page(pathname):
    if pathname == '/board':
        #from apps import card_modal, charts
        return card_modal.layout, charts.layout
    if pathname == '/1':
        return scc.layout   # upload.component layout
    if pathname == '/2':
        #from apps.charts import layout
        return 'layout'
    if pathname == '/3':
        return "Pie charts coming soon"
    else:
        return "404"  
# toggle pages callback--------------------------------------------------------------------------------


#csv uploader to hidden div---------------------------------------------------------------------------
# retrieve the contents from the upload component and store it in a hidden div as a list of serialized json objects( dict like, orient='columns )
@app.callback(Output('div-data', 'children'), #[Output('store', 'data'), 
            [Input('upload-data', 'contents')],
            [State('upload-data', 'filename'),
            State('upload-data', 'last_modified')] # , State('store', 'data')
)
@cache.memoize()            
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            scc.parse_contents(c, n, d) for c, n, d in 
            zip(list_of_contents, list_of_names, list_of_dates)]

        return children  # returns a list of a json orient='column' string
#csv uploader to hidden div---------------------------------------------------------------------------

#csv table uploader---------------------------------------------------------------------------
# retrieve the contents from the hidden div, unserialize it, put into table component and show in seperate div
@app.callback(Output('table', 'children'),
            [Input('div-data', 'children')],
            #[State('store', 'data')]
)
def table(div_data):
    # json_object is a list <class 'list'>
    #print(div_data)
    if div_data is None:
        raise PreventUpdate
    else:
        # div_data is a list of json object/s (could be more than 1)
        df = pd.read_json(div_data[0], orient='columns') # deserialised dataframe
        return html.Div([dash_table.DataTable(
                    data= df.to_dict('records'),
                    columns=[{'name': i, 'id': i} for i in df.columns]
                    )          
                ])
#csv table uploader---------------------------------------------------------------------------

#charts uploader---------------------------------------------------------------------------
# retrieve the contents from the hidden div, unserialize it, put into a fuction to create new df, return a graph
@app.callback(Output('charts', 'children'),
            [Input('div-data', 'children')],
)
def dashboard_charts(div_data):

    colors = {
    'background': '#111111',
    'text': '#8E3DEB'
    }

    if div_data is None:
        return html.Div(
                    html.H1('load csv file')
        )
        #raise PreventUpdate
    
    else:
        # div_data is a list of a json object (should only be 1)
        df = pd.read_json(div_data[0], orient='columns') # deserialised dataframe
        #print(df)
        current_holdings = cd.cumsum_total_income(df)
        daily_income = cd.daily_roi_income(df)
        daily_income_bar = cd.daily_roi_income(df)
        #line = px.line(current_holdings, x="Date", y="Holdings", title='Current holdings')
        #print(current_holdings)
        line = px.line(current_holdings, x="Date", y="Credit", title='Current holdings')
        bar = px.bar(daily_income_bar, x="Date", y=["Credit","Debit"], barmode="group")
        pie = px.pie(df, values="Credit", names="Remark", title="All Bonuses")
        
    return html.Div(style={'backgroundColor': colors['background']}, 
            children=   
                [
                    dcc.Graph(
                        id='line-graph',
                        figure=line
                    ),

                    dcc.Graph(
                        id='bar-graph',
                        figure=bar
                    ),

                    dcc.Graph(
                        id='pie-chart',
                        figure=pie
                    )
                ]
    )
#charts uploader---------------------------------------------------------------------------

#card modal--------------------------------------------------------------------------------
@app.callback(
    [Output('col1', 'style'), Output("modal-1", "is_open"), Output("data1", "children")],
    [Input("div-data", "children"), Input("open-1", "n_clicks"), Input("close-1", "n_clicks")],
    [State("modal-1", "is_open")]
)
def toggle_modal_1(div_data, n1, n2, is_open):
    if div_data is None:
        #raise PreventUpdate
        return {'display': 'none'}, None, None
    else:
        df = pd.read_json(div_data[0], orient='columns') # deserialised dataframe
        data = cd.sum_roi_income(df)
        if n1 or n2:
            return {'display': 'block'}, not is_open, data
        return {'display': 'block'}, is_open, data     

@app.callback(
    [Output('col2', 'style'), Output("modal-2", "is_open"), Output("data2", "children")],
    [Input("div-data", "children"), Input("open-2", "n_clicks"), Input("close-2", "n_clicks")],
    [State("modal-2", "is_open")]
)
def toggle_modal_2(div_data, n1, n2, is_open):
    if div_data is None:
        #raise PreventUpdate
        return {'display': 'none'}, None, None
    else:
        df = pd.read_json(div_data[0], orient='columns') # deserialised dataframe
        data = cd.sum_binary_income(df)
        if n1 or n2:
            return {'display': 'block'}, not is_open, data
        return {'display': 'block'}, is_open, data     

@app.callback(
    [Output('col3', 'style'), Output("modal-3", "is_open"), Output("data3", "children")],
    [Input("div-data", "children"), Input("open-3", "n_clicks"), Input("close-3", "n_clicks")],
    [State("modal-3", "is_open")]
)
def toggle_modal_3(div_data, n1, n2, is_open):
    if div_data is None:
        #raise PreventUpdate
        return {'display': 'none'}, None, None
    else:    
        df = pd.read_json(div_data[0], orient='columns') # deserialised dataframe
        data = cd.sum_total_income(df)
        if n1 or n2:
            return {'display': 'block'}, not is_open, data
        return {'display': 'block'}, is_open, data     
#card modal---------------------------------------------------------------------------


if __name__ == '__main__':
    app.run_server(debug=True)