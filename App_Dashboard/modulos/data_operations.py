# Loading Data Module

# Imports
import json
import pandas as pd
import pathlib
import datetime
from modulos import constant, app_element

# Dataframe Generator Module
def generate_dataframe():
    
    # Load File
    DATAFRAME_MAIN = pd.read_csv(constant.DATAFILE)

    # Columns Mapping
    DATAFRAME_MAIN.rename(constant.FIELD_MAP, axis = 1, inplace = True)

    # Date Column Formatation 
    DATAFRAME_MAIN[constant.DATA_CRIACAO] = pd.to_datetime(DATAFRAME_MAIN[constant.DATA_CRIACAO], format = constant.DATE_FORMAT)
    DATAFRAME_MAIN[constant.DATA_FECHAMENTO] = pd.to_datetime(DATAFRAME_MAIN[constant.DATA_FECHAMENTO], format = constant.DATE_FORMAT)

    # Add the formatted columns to the dataframe 
    DATAFRAME_MAIN[constant.DATA_CRIACAO] =  DATAFRAME_MAIN[constant.DATA_CRIACAO].dt.date
    DATAFRAME_MAIN[constant.DATA_FECHAMENTO] =  DATAFRAME_MAIN[constant.DATA_FECHAMENTO].dt.date

    # Filter by status column 
    DATAFRAME_MAIN.loc[DATAFRAME_MAIN.eval('Status != @constant.CLOSED_ISSUE_STATUS'), constant.STATUS_TYPE] = "Aberto"
    DATAFRAME_MAIN.loc[DATAFRAME_MAIN.eval('Status == @constant.CLOSED_ISSUE_STATUS'), constant.STATUS_TYPE] = "Fechado"

    return(DATAFRAME_MAIN)

# Open Calls Function
def get_open_issues(dataframe):
    return (dataframe.query('Status != @constant.CLOSED_ISSUE_STATUS'))

# Closed Calls Function
def get_closed_issues(dataframe):
    return (dataframe.query('Status == @constant.CLOSED_ISSUE_STATUS'))

# Columns Fit Functio
def read_config_in_df():

    # Loads the constant file
    constant.read_config()  

    # Data Preparation
    data = [
                ['id', constant.ID, constant.CSV_ID],
                ['status', constant.STATUS, constant.CSV_STATUS],
                ['criado_por', constant.CRIADO_POR, constant.CSV_CRIADO_POR],
                ['atribuido_a', constant.ATRIBUIDO_A, constant.CSV_ATRIBUIDO_A],
                ['atendido_por', constant.ATENDIDO_POR, constant.CSV_ATENDIDO_POR],
                ['severidade', constant.SEVERIDADE, constant.CSV_SEVERIDADE],
                ['prioridade', constant.PRIORIDADE, constant.CSV_PRIORIDADE],
                ['cliente', constant.CLIENTE, constant.CSV_CLIENTE],
                ['data_criacao', constant.DATA_CRIACAO, constant.CSV_DATA_CRIACAO],
                ['data_fechamento', constant.DATA_FECHAMENTO, constant.CSV_DATA_FECHAMENTO],
                ['tipo_chamado', constant.TIPO_CHAMADO, constant.CSV_TIPO_CHAMADO]
            ]
    
    # New dataframe
    df = pd.DataFrame(data, columns = ['Id Coluna', 'Nome Coluna', 'Mapeado Para'])

    return (df)

# Recording the mapping file
def write_field_mapping_file(data, dt_format):
    JSON_FILE = {}
    JSON_FILE['KeyMapping'] = {}
    JSON_FILE['KeyMapping']['VarMapping'] = {}
    JSON_FILE['KeyMapping']['FieldMapping'] = {}

    for item in data:
        JSON_FILE['KeyMapping']['VarMapping'].update({item['Id Coluna'].rstrip(): item['Nome Coluna'].rstrip()})
        JSON_FILE['KeyMapping']['FieldMapping'].update({item['Mapeado Para'].rstrip(): item['Nome Coluna'].rstrip()})
    
    JSON_FILE["DateFormat"] = dt_format
    with open(constant.MAPPING_FILE, "w") as f:
        json.dump(JSON_FILE, f, indent = 3)
    
    return 0