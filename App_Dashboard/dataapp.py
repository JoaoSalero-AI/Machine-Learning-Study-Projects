# Main File for the Data App

# Imports
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# Load the app's connection file
from app import app
from app import server

# Conect to the pages and other modules
from pages import dashboard, overview, settings
from modulos import navbar, constant

# Load the configurations
CONFIG_OBJECT = constant.read_config()

# Main Content
content = html.Div(id = "page-content", style = constant.CONTENT_STYLE, className = "p-3 pt-4 pb-3")

# Layout
app.layout = html.Div([dcc.Location(id = "url"), navbar.layout, content])

# Callback
@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/pages/dashboard' or pathname == '/':
        return dashboard.get_layout()
    elif pathname == '/pages/overview':
        return overview.get_layout()
    elif pathname == '/pages/settings':
        return settings.get_layout()
    else:
        return dbc.Jumbotron(
            [
                html.Div([
                    html.H1("404: Not found", className = "text-danger"),
                    html.Hr(),
                    html.P(f"Pagina {pathname} não encontrada...")
                ],
                style = constant.NAVITEM_STYLE)
            ]
       )

# Title
app.title = 'Data App - Interactive Dashboard for Support Call Analysis' 

#  Execute the app
if __name__ == '__main__':
    app.run_server(debug = False, port = 3000, host = '0.0.0.0', threaded = True)


