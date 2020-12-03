
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.CardFooter import CardFooter
from dash_bootstrap_components._components.CardHeader import CardHeader
from dash_bootstrap_components._components.Col import Col
import dash_html_components as html
import dash
from dash.dependencies import Input, Output, State



# app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP], # switch BOOTSTRAP for SOLAR
# )
#from app import app, server

'''
there are a couple of ways to create a layout.
in this example two variables are created, 1st content, to deal with all the bootstrap 
components then 2nd 'layout', to deal with the html components of the layout. notice though that
in the 'layout' variable there is still some bootstrap component modeling. This is not neccessary
to be done here. That is why I have done two variations, one where all bootstrap modeling is done 
in one variable like in 'content1' and some where the modeling is in both variables 'content2' &
'content3'
'''

#print(cc.sum_roi_income(location2))

content1 =  dbc.Card(
        [
            CardHeader('Daily ROI'),
            dbc.CardBody(
                [
                    html.H4("Card title", className="card-title"),
                    html.P(id='data1', className="card-text"),
                ]
            ),
            dbc.CardFooter(
                [
                    dbc.Button("Info", id="open-1", color="primary"),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("Header"),
                            dbc.ModalBody("Total return on trading pool holdings only for present moment"),
                            dbc.ModalFooter(
                                dbc.Button("Close", id="close-1", className="ml-auto")
                            ),
                        ], id="modal-1",
                    )
                ]    
            ),
        ], inverse=False
)


content2 = dbc.Card(
        [
            CardHeader('Daily ROI'),
            dbc.CardBody(
                [
                    html.H4("Card title", className="card-title"),
                    html.P(id='data2', className="card-text"),
                ]    
            ),
            dbc.CardFooter(
                [    
                    dbc.Button("Info", id="open-2", color="primary"),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("Header"),
                            dbc.ModalBody("Total return from binary bonus"),
                            dbc.ModalFooter(
                                dbc.Button("Close", id="close-2", className="ml-auto")
                            ),
                        ], id="modal-2",
                    )
                ]
            ), 
        ], inverse=False
)


content3 =  dbc.Card(
        [
            CardHeader('Daily ROI'),
            dbc.CardBody(
                [
                    html.H4("Card title", className="card-title"),
                    html.P(id='data3', className="card-text"),
                ]    
            ),
            dbc.CardFooter(  
                [
                    dbc.Button("Info", id="open-3", color="primary"),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("Header"),
                            dbc.ModalBody("Sum of incomes for present time"),
                            dbc.ModalFooter(
                                dbc.Button("Close", id="close-3", className="ml-auto")
                            ),
                        ], id="modal-3",
                    )
                ]
            ),
    ], inverse=False
)

layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(content1, id='col1', style= {'display': 'none'}),
                dbc.Col(content2, id='col2', style= {'display': 'none'}),
                dbc.Col(content3, id='col3', style= {'display': 'none'})
            ]
        )
    ],#id='card-div', style= {'display': 'block'}
)



#html.Div(id='modals')

# app.layout = html.Div(layout)

# def toggle_modal(n1, n2, is_open):
#     if n1 or n2:
#         return not is_open
#     return is_open, is_open, is_open

# app.callback(
#     [Output("modal-1", "is_open"), Output("modal-2", "is_open"), Output("modal-3", "is_open")],
#     [Input("open-1", "n_clicks"), Input("close-1", "n_clicks")],
#     [State("modal-1", "is_open")]
# )(toggle_modal)


# if __name__ == "__main__":
#     app.run_server(debug=True)