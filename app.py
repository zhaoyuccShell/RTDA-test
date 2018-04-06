import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from components import Column, Header, Row
import config
from auth import auth
from utils import StaticUrlPath


app = dash.Dash(
    __name__,
    # Serve any files that are available in the `static` folder
    static_folder='static'
)
auth(app)

server = app.server  # Expose the server variable for deployments

# Standard Dash app code below
app.layout = html.Div(className='container', children=[

    Header('Sample App'),

    Row([
        Column(width=4, children=[
            dcc.Dropdown(
                id='dropdown',
                options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
                value='LA'
            )
        ]),
        Column(width=8, children=[
            dcc.Graph(id='graph')
        ])
    ])
])

@app.callback(Output('graph', 'figure'),
              [Input('dropdown', 'value')])
def update_graph(value):
    return {
        'data': [{
            'x': [1, 2, 3, 4, 5, 6],
            'y': [3, 1, 2, 3, 5, 6]
        }],
        'layout': {
            'title': value,
            'margin': {
                'l': 60,
                'r': 10,
                't': 40,
                'b': 60
            }
        }
    }

# Optionally include CSS
app.css.append_css({
    'external_url': [
        StaticUrlPath(css) for css in [
            'dash.css', 'grid.css', 'loading.css', 'page.css',
            'spacing.css', 'styles.css', 'tables.css', 'typography.css'
        ]
    ]
})

if __name__ == '__main__':
    app.run_server(debug=True)
