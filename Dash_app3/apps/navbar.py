from os import link
import dash
import dash_bootstrap_components as dbc

#app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
#from app import app

layout = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Load csv/xml", href="/1")),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("More pages", header=True),
                    dbc.DropdownMenuItem("Tree", href="/2"),
                    dbc.DropdownMenuItem("Pie Chart", href="/3"),
                ],
                nav=True,
                in_navbar=True,
                label="More",
            ),
        ],
        brand="Dashboard",
        brand_href="/board",
        color="primary",
        dark=True,
)
