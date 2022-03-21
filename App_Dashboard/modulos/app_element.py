# Módulo para gerar a tabela de dados no Dash

# Imports
import dash
import dash_table
import dash_html_components as html
import pandas as pd

# Dash Table Generator
def generate_dashtable(identifier, dataframe):
    return dash_table.DataTable(id = identifier,
                                columns = [{"name": i, "id": i} for i in dataframe.columns],
                                data = dataframe.to_dict('records'),
                                filter_action = "native",
                                style_header = {'fontWeight': 'bold'},
                                style_cell = {'whiteSpace': 'normal', 'height':'auto'},
                                fixed_rows = {'headers': True},
                                page_action = 'none',
                                style_table = {'height': '300px','width': 'auto'})