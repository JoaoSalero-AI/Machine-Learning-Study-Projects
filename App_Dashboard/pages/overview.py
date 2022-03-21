# Overview Page

# Imports
import traceback
import pandas as pd
import dash
import dash_table
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

# Customized Modules
from app import app
from modulos import app_element, data_operations, constant

# Layout Function
def get_layout():
	
	try:  

		# Dataframe Preparation
		df = data_operations.generate_dataframe()
		df1 = df[[constant.ATRIBUIDO_A, constant.ID]]
		df1 = df1.groupby([constant.ATRIBUIDO_A])[constant.ID].count().reset_index(name = "Total")
		df2 = df[[constant.ATENDIDO_POR, constant.ID]]
		df2 = df2.groupby([constant.ATENDIDO_POR])[constant.ID].count().reset_index(name = "Total")

		# Layout
		layout = dbc.Container([
			     dbc.Row([
						dbc.Col([
						dbc.Card([dbc.CardHeader("Dashboard Objective"),
								  dbc.CardBody([html.H2("Data App", className = "card-text")]),], className = "shadow p-3 bg-light rounded")], width = 3),
						dbc.Col([
						dbc.Card([dbc.CardHeader("Number of Calls Analyzed"),
								  dbc.CardBody([html.H2("300", className = "card-text")]),], className = "shadow p-3 bg-light rounded")], width = 3),
						dbc.Col([
						dbc.Card([dbc.CardHeader("Data Collection Period"),
								  dbc.CardBody([html.H2("2020-2021", className = "card-text")]),], className = "shadow p-3 bg-light rounded")], width = 3),
						dbc.Col([
						dbc.Card([dbc.CardHeader("If in doubt, send an email to:"),
								  dbc.CardBody([html.H2("Customer Support", className = "card-text")]),], className = "shadow p-3 bg-light rounded")], width = 3)],
						className= "pb-3"),
				 dbc.Row([
						dbc.Col(dbc.Card([
								dbc.CardHeader(f"Total Calls Per {constant.ATRIBUIDO_A}"),
								app_element.generate_dashtable(identifier = "table1", dataframe = df1)],
								className = "shadow p-3 bg-light rounded"), width = 6),
						dbc.Col(dbc.Card([
								dbc.CardHeader(f"Total Calls Per {constant.ATENDIDO_POR}"),
								app_element.generate_dashtable(identifier = "table2", dataframe = df2)],
								className = "shadow p-3 bg-light rounded"), width = 6)
				])
		],
		fluid = True)

		return layout
	except:
		layout = dbc.Jumbotron(
					[
						html.Div([
							html.H1("500: Internal Server Error", className="text-danger"),
							html.Hr(),
							html.P("O seguinte erro ocorreu:"),
                            html.Code(traceback.format_exc())
						],
						style=constant.NAVITEM_STYLE)
					]
				)
		return layout


