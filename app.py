import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
import os
import plotly.plotly as py
import dash_auth

import config

app = dash.Dash(__name__)

# Checks if running inside Plotly On-Premise environment
if 'DYNO' in os.environ:
    if config.PATH_BASED_ROUTING:
        if config.DASH_APP_NAME == 'name-of-your-dash-app':
             raise Exception('Please enter the name of your dash app inside config.py')
        app.config.requests_pathname_prefix = '/{}/'.format(
            config.DASH_APP_NAME
        )

if config.PATH_BASED_ROUTING:
    APP_URL = '{}/{}'.format(
        config.PLOTLY_DASH_DOMAIN.strip('/'),
        config.DASH_APP_NAME,
    )
else:
    APP_URL = '{}://{}.{}'.format(
        config.PLOTLY_DASH_DOMAIN.split('://')[0],
        config.DASH_APP_NAME,
        config.PLOTLY_DASH_DOMAIN.split('://')[1].strip('/')
    )

dash_auth.PlotlyAuth(
    app,
    config.DASH_APP_NAME,
    config.DASH_APP_PRIVACY,
    APP_URL
)


# Expose the server variable
server = app.server

# Serve JS and CSS files locally instead of from global CDN
# app.scripts.config.serve_locally = True
# app.css.config.serve_locally = True

# Standard Dash app code below
app.layout = html.Div([
    html.H2('Hello World'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='display-value')
])

@app.callback(dash.dependencies.Output('display-value', 'children'),
              [dash.dependencies.Input('dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)
