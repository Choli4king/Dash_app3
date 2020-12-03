#%%
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

#from app import app, cache

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# cache = Cache(app.server, config={
#     'CACHE_TYPE': 'filesystem',
#     'CACHE_DIR': 'cache-directory'
# })
#cache.init_app(app.server, config=CACHE_CONFIG)
#%%

layout = html.Div(
    [
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Drag and Drop or ',
                html.A('Select Files')
            ]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px'
            },
            # Allow multiple files to be uploaded
            multiple=True
        ), 
        #html.Div(id='graph'),
        #html.Div(id='output-data-upload', style={'display': 'none'}),
        html.Div(id='table'),
        #html.Div(id='div-data'),
    ]
)



def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',') #this step need the zip object from the callback

    decoded = base64.b64decode(content_string)
    try:
        # Assume that the user uploaded a CSV file
        df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return df.to_json(orient="columns")     # <class 'str'>




# def dataframe(contents, filename, date):
#     #print(pd.read_json(query_data(), orient='split'))
#     return pd.read_json(parse_contents(contents, filename, date), orient='split')    

# # @app.callback(Output('output-data-upload', 'children'),
# #             [Input('upload-data', 'contents')],
# # )
# # def update_output(list_of_contents):
# #     #print(contents)
# #     if list_of_contents is not None:
# #         children = [
# #             parse_contents(c) for c in
# #             zip(list_of_contents)]
# #         return children

#

# # retrieve the contents from the upload component and store it in a hidden div as a list of serialized json objects( dict like, orient='columns )
# @app.callback(Output('output-data-upload', 'children'),
#             [Input('upload-data', 'contents')],
#             [State('upload-data', 'filename'),
#             State('upload-data', 'last_modified')])
# @cache.memoize()            
# def update_output(list_of_contents, list_of_names, list_of_dates):
#     if list_of_contents is not None:
#         children = [
#             parse_contents(c, n, d) for c, n, d in
#             zip(list_of_contents, list_of_names, list_of_dates)]
#         #print(children) 
#         return children  # returns a list of json orient='column' strings
# #%%

# #%%
# # retrieve the contents from the hidden div, unserialize it, and show in seperate div
# @app.callback(Output('output-data-upload-1', 'children'),
#             [Input('output-data-upload', 'children')],
# )
# def update_output_2(div_data):
#     # json_object is a list <class 'list'>
#     #print(div_data)
#     if div_data is None:
#         raise PreventUpdate
#     else:
#         # div_data is a list of json object/s (could be more than 1)
        
#         #for x in div_data:
#             #children = x #pd.read_json(stored_data)
#             #print(json_object)
#             #return x

#         #x = json.loads(div_data[0])    
#         #print(type(x))
#         #x = json.dumps(x, indent=2)
#         #df = pd.read_json(div_data[0], orient='columns') # deserialised dataframe
#         #print(df)
#         #json_object = div_data[0] # json_object is a str <class 'str'>
#         #print(type(json_object))
        
#         #print(div_data["Sr No."])
#         #print(div_data)

#         #json_object = pd.DataFrame.from_dict(div_data, orient='index')
#         #print(json_object)
#         x = div_data

#     return x #json_object        
# #%%


# #%%
# # retrieve the contents from the hidden div, unserialize it
# @app.callback(Output('graph', 'children'),
#             [Input('output-data-upload', 'children')],
# )
# def graph(div_data):
#     #print(contents)
#     if div_data is None:
#         raise PreventUpdate
#     else:
#         # div_data is a list of json object/s (could be more than 1)
#         #df = pd.read_json(div_data, orient='columns') # deserialised dataframe
#         #print(df)
#         current_holdings = cd.cumsum_total_income(div_data)
#         #line = px.line(current_holdings, x="Date", y="Holdings", title='Current holdings')
#         #print(current_holdings)
#         line = px.line(current_holdings, x="Date", y="Credit", title='Current holdings')
        
#     return dcc.Graph(id ='example-graph-2', figure=line) 


# if __name__ == '__main__':
#     app.run_server(debug=True)