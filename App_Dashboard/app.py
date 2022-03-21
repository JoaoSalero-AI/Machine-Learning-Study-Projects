# Dash Server 

# Import
import dash

# meta_tags: to be responsive
app = dash.Dash(__name__, suppress_callback_exceptions = True, meta_tags = [{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}])

# Creating server
server = app.server
