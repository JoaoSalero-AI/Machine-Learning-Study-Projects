# Dashboard Script
# https://dash.plotly.com/dash-html-components

# Imports
import traceback
import pandas as pd
import plotly.express as px
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

# Customized Modules
from app import app
from modulos import data_operations, constant

# Layout Gen
def get_layout():

    try:

        # Load the data
        df_issues = data_operations.generate_dataframe()

        # Group the data
        df1 = df_issues.groupby([constant.STATUS])[constant.ID].count().reset_index(name = "Total Chamados")
        grp = df_issues.groupby([constant.DATA_CRIACAO, constant.TIPO_CHAMADO])[constant.ID]
        df2 = grp.count().reset_index(name = "Total Chamados")
        df3 = df_issues.groupby([constant.PRIORIDADE])[constant.ID].count().reset_index(name = "Total Chamados")

        # Container Generator
        layout = dbc.Container([
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id = 'my-line', 
                                      figure = px.line(df2, 
                                                       x = constant.DATA_CRIACAO, 
                                                       y = 'Total Chamados', 
                                                       color = constant.TIPO_CHAMADO,
                                                       title = 'Chamados de Suporte Por Data de Criação'))
                        ],
                        width=12)
                    ],
                    style = {'padding-bottom': '10px'},
                    no_gutters = True),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id = 'my-pie2', 
                                      figure = px.pie(df3, 
                                                      values = 'Total Chamados', 
                                                      names = constant.PRIORIDADE, 
                                                      title = 'Chamados de Suporte Por Prioridade',
                                                      hole = 0.3))
                        ],
                        width = 6),
                        dbc.Col([
                            dcc.Graph(id = 'my-pie', 
                                      figure = px.pie(df1, 
                                                      values = 'Total Chamados', 
                                                      names = constant.STATUS,
                                                      title = 'Chamados de Suporte Por Status'))
                        ],
                        width = 6)
                    ],
                    style = {'padding-bottom': '10px'},
                    no_gutters = True)
                ],
                fluid = True)
        return layout
    except:
        layout = dbc.Jumbotron(
                    [
                        html.Div([
                            html.H1("500: Internal Server Error", className = "text-danger"),
                            html.Hr(),
                            html.P(f"Following Exception Occured: "),
                            html.Code(traceback.format_exc())
                        ],
                        style = constant.NAVITEM_STYLE)
                    ]
                )
        return layout
